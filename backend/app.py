from flask import Flask, request
import json
from scripts import check_cluster_change
from scripts import create_deployment_from_template, build_and_push_image, clone_repo
import os
import shutil

app = Flask(__name__)

# body = [
# 	{
# 		"name":"cluser-1",
# 		"provider":"AKS",
# 		"numberOfHosts":2,
# 		"apps":[
# 			{
# 				"name":"test",
# 				"replicas":3
# 			}
# 		]
# 	}
# 	]

@app.get("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.post("/submit")
def submit():
	body = request.get_json()
	data = json.load(body)
	check_cluster_change(data)
	for cluster in data:
		for app in cluster['apps']:
			# creating folder
			folder = f"./temp/{cluster['provider']}-{cluster['name']}"
			os.makedirs(folder, mode=511, exist_ok=True)

			# run scripts here
			clone_repo(app['app'], app['github_url'], folder)
			build_and_push_image(app['app'], folder)
			create_deployment_from_template("deployment", folder, app['name'])

			# delete folder
			shutil.rmtree(folder)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

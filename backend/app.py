from flask import Flask, request, jsonify
from scripts import check_cluster_change
from scripts import build_and_push_image, clone_repo
from scripts import create_deployment_from_template, apply, create_lb_from_template, get_lb_endpoint
import os
import shutil

app = Flask(__name__)

# body = [
# 	{
# 		"name":"cluser-1",
# 		"provider":"EKS",
# 		"numberOfHosts":2,
# 		"apps":[
# 			{
# 				"name":"test",
# 				"replicas":3
# 			}
# 		]
# 	}
# 	]

# response = [
# 	{
# 		"name": "cluster-1"
# 		"lbs": [
# 			{"name": "test1", "lbURL":"URL1" },
# 			{"name": "test2", "lbURL":"URL2" },
# 		]
# 	}
# ]

@app.get("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.post("/submit")
def submit():
	data = request.get_json()
	#Makes changes to the cluster
	check_cluster_change(data)

	response = []

	for cluster in data:
		cluster_resp = {"name":cluster['name'], "lbs":[]}

		# creating folder
		folder = f"./temp/{cluster['provider']}-{cluster['name']}"
		os.makedirs(folder, mode=511, exist_ok=True)
		for app in cluster['apps']:
			# run scripts here
			clone_repo(app['name'], app['github_url'], folder)
			build_and_push_image(app['name'], folder)
			create_deployment_from_template("deployment", folder, app['name'], app['replicas'])
			create_lb_from_template("deployment", folder, app['name'])
			apply(folder)
			
			# geting lb url
			lbURL = get_lb_endpoint(app['name'])

			# constructing response
			cluster_resp['lbs'].append({"name":app['name'], "lbURL": lbURL})

		response.append(cluster_resp)

		# delete folder
		shutil.rmtree(folder)

		return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

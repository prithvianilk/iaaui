from flask import Flask, request, jsonify
import json
from scripts import create_deployment_from_template

app = Flask(__name__)

@app.get("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.post("/submit")
def submit():
	body = request.get_json()
	data = json.load(body)
	for cluster in data:
		for app in cluster.apps:
			create_deployment_from_template("deployment", app['name'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
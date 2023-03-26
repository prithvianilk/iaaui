import jinja2
import subprocess
import time

def create_lb_from_template(template_file, folder, image_name):
	print("Creating lb service...")
	templateLoader = jinja2.FileSystemLoader(searchpath="./k8s")
	templateEnv = jinja2.Environment(loader=templateLoader)
	template = templateEnv.get_template(template_file)

	output_text = template.render({"image_name": image_name})  # this is where to put args to the template renderer
	# to save the results
	with open(f"{folder}/{template_file}-{image_name}.yaml", "w") as f:
		f.write(output_text)

def get_lb_endpoint(image_name):
	output = ''
	while output == '\'\'':
		response = subprocess.run(["kubectl", "get" ,"svc" ,f"{image_name}-loadbalancer", "-o=jsonpath='{.status.loadBalancer.ingress[0].hostname}'"], text=True, capture_output=True)
		output = response.stdout
		print(output, response.stderr)
		time.sleep(5)
	return output
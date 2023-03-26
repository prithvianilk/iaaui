import jinja2
import os

def create_deployment_from_template(template_file, folder, image_name, replicas):
	print("creating deployment...")
	templateLoader = jinja2.FileSystemLoader(searchpath="./k8s")
	templateEnv = jinja2.Environment(loader=templateLoader)
	template = templateEnv.get_template(template_file)

	output_text = template.render({"image_name": image_name, "replicas":replicas})  # this is where to put args to the template renderer
	# to save the results
	with open(f"{folder}/{template_file}-{image_name}.yaml", "w") as f:
		f.write(output_text)

def apply(folder):
	print("applying yamls to k8s")
	print('folder:', folder)
	os.system(f"kubectl apply -f {folder}")
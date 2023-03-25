import json
import os

def create_terraform_files():
    path=create_temp_folder()
    # with open("../terraform/terraform.tfvars.json","r") as template_file:
    #     template_file_data=json.load(template_file)
    # template_file_data["cluster_name"]=cluster_name
    # template_file_data["min_size"]=min_size
    # template_file_data["max_size"]=max_size
    # template_file_data["desired_size"]=desired_size
    # template_file_data["instance_type"]=instance_type
    # template_file_data["node_group_name"]=node_group_name
    # with open(f'../{path}/terraform.tfvars.json', 'w') as fp:
    #     json.dump(template_file_data, fp)


def create_temp_folder():
    print(os.cwd)
#cluster_name,min_size,max_size,desired_size,instance_type,node_group_name
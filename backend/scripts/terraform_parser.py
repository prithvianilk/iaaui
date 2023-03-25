import json
import os
import shutil

def create_terraform_files(cluster_name,min_size,max_size,desired_size,instance_type,node_group_name):
    path=create_temp_folder(cluster_name)
    with open(f"{os.getcwd()}/terraform/terraform.tfvars.json","r") as template_file:
        template_file_data=json.load(template_file)
    template_file_data["cluster_name"]=cluster_name
    template_file_data["min_size"]=min_size
    template_file_data["max_size"]=max_size
    template_file_data["desired_size"]=desired_size
    template_file_data["instance_type"]=instance_type
    template_file_data["node_group_name"]=node_group_name
    with open(f'{path}/terraform.tfvars.json', 'w') as fp:
        json.dump(template_file_data, fp)
    backend_data=open(f'{path}/backend.tf','w')
    backend_text='''terraform{{
    backend "s3"{{
        region="ap-south-1"
        bucket="yg-hack-s3"
        key="{}-terraformstate/terraform.tfstate"
        access_key = "AKIA3EZCPWK3H2I2TYWH"
        secret_key = "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"
    }}
}}'''.format(cluster_name)
    backend_data.write(backend_text)


def create_temp_folder(cluster_name):
    if not os.path.exists(os.path.join(os.getcwd(),"temp_tf",cluster_name)):
        os.mkdir(os.path.join(os.getcwd(),"temp_tf",cluster_name))
    shutil.copyfile(os.path.join(os.getcwd(),"terraform/main.tf"),os.path.join(os.getcwd(),"temp_tf",cluster_name,"main.tf"))
    shutil.copyfile(os.path.join(os.getcwd(),"terraform/output.tf"),os.path.join(os.getcwd(),"temp_tf",cluster_name,"output.tf"))
    shutil.copyfile(os.path.join(os.getcwd(),"terraform/provider.tf"),os.path.join(os.getcwd(),"temp_tf",cluster_name,"provider.tf"))
    shutil.copyfile(os.path.join(os.getcwd(),"terraform/variable.tf"),os.path.join(os.getcwd(),"temp_tf",cluster_name,"variable.tf"))
    return os.path.join(os.getcwd(),"temp_tf",cluster_name)
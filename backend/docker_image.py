import os

def clone_repo(image_name, github_url):
    os.system(f'git clone {github_url} temp/{image_name}')


def push_image(image_name, github_url):
    pass

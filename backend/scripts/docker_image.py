import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def clone_repo(image_name, github_url, base_folder):
    os.system(f'git clone {github_url} {base_folder}/{image_name}')


def build_and_push_image(image_name, base_folder):
    os.system(f'./push_docker_image.sh {image_name} {base_folder}')


if __name__ == "__main__":
    clone_repo("yg-example-app", "https://github.com/prithvianilk/yg-example-app", "./temp/1")
    build_and_push_image("yg-example-app", './temp/1')
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def clone_repo(image_name, github_url):
    os.system(f'git clone {github_url} temp/{image_name}')


def build_and_push_image(image_name):
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', default=None)
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', default=None)
    os.system(
        f'./push_docker_image.sh {image_name} {aws_access_key_id} {aws_secret_access_key}')


if __name__ == "__main__":
    clone_repo("yg-example-app", "https://github.com/prithvianilk/yg-example-app")
    build_and_push_image("yg-example-app")

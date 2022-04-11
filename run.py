import subprocess
from loguru import logger
import json


with open('config.json') as f:
    config = json.load(f)
model_name = config["model_name"]


def run():
    subprocess.call('python model_utils.py', shell=True)
    subprocess.call('bentoml build')
    subprocess.call(
        f'bentoml containerize -t {model_name}:latest {model_name}:latest', shell=True)
    subprocess.call(f'docker run -p 5000:5000 {model_name}:latest', shell=True)


if __name__ == '__main__':
    run()

import json
import bentoml
from deployable import DeployableModel
from bentoml.io import NumpyNdarray
import numpy as np

with open('config.json') as f:
    config = json.load(f)

model_path = config["model_path"]
model_framework = config["model_framework"]
model_name = config["model_name"]

model = DeployableModel(model_path)

if model_framework == 'sklearn':
    import bentoml.sklearn
    tag = bentoml.sklearn.save(model_name, model.model)
elif model_framework == 'xgboost':
    pass
elif model_framework == 'tf':
    pass
elif model_framework == 'torch':
    pass

# with open('bento-setup.txt', 'w') as file:
#     file.write(str(tag))

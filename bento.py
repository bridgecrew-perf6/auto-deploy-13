import json
import bentoml
from bentoml.io import NumpyNdarray
import numpy as np

with open('config.json') as f:
    config = json.load(f)

model_framework = config["model_framework"]
model_name = config["model_name"]

if model_framework == 'sklearn':
    import bentoml.sklearn
    runner = bentoml.sklearn.load_runner(f'{model_name}:latest')
elif model_framework == 'xgboost':
    pass
elif model_framework == 'tf':
    pass
elif model_framework == 'torch':
    pass


svc = bentoml.Service(model_name, runners=[runner])


@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def predict(input_ndarray: np.ndarray) -> np.ndarray:
    # Define pre-processing logic
    result = runner.run(input_ndarray)
    # Define post-processing logic
    return result

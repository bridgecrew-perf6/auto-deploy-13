import pickle


class DeployableModel:
    def __init__(self, model_path) -> None:
        '''
            Inputs:
                model_path : str -> Path to pickled model file
                Currently only working with pickle
        '''
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

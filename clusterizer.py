import pandas as pd
import sklearn.cluster
import yaml

class Clusterizer():
    def __init__(self, path, alg, config):
        self.alg = alg
        self.path = path
        self.config = config

    def load_data(self):
        df = pd.read_csv(self.path)
        self.X = df.values

    def load_params(self, params=None):
        if self.config:
            params =

        else:
            with open('self.config', 'r') as f:
                params = yaml.load(f, Loader=yaml.SafeLoader)

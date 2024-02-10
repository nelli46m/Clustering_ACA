import argparse
import yaml
import inspect
from clusterizer import Clusterizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path')
    parser.add_argument('--algo')
    parser.add_argument('--config', default=None)
    args = parser.parse_args()
    path = args.path
    algo = args.algo
    config = args.config

    prep = Clusterizer(path, algo, config)
    if algo.lowercase() == "all":
        if config == None:
            raise "You should have config file."
        else:
            with open('config', 'r') as f:
                params = yaml.load(f, Loader=yaml.SafeLoader)
    else:
        if config:
            prep = Clusterizer.load_params()

        # if config == None:
        #     model = Clusterizer.model(alg)
        #     for m in model:
        #         hyperparams = inspect.getargspec()(m.__init__).args
        #         print(hyperparams)
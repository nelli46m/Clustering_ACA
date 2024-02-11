import argparse
import yaml
import inspect
from clusterizer import Clusterizer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help="Path of data that should be clusterized")
    parser.add_argument('--algo', help="Name of the algorithm to use.")
    parser.add_argument('--config', default=None)
    args = parser.parse_args()
    path = args.path
    algo = args.algo
    config = args.config

    prep = Clusterizer(path, algo, config)
    Clusterizer.load_data()
    if config is None and algo == "all":
        raise "You should have config file."
    elif config is None and algo != 'all':
        print('Please insert values for any of these attributes (default values will be used otherwise):')
        print(Clusterizer.hyperparameters())
        parser.add_argument('hyperparameters', nargs='+', metavar=('name', 'value'),
                            help='Specify hyperparameter name and value. Alternating pairs of name and value.')
        params = parser.parse_args()
        Clusterizer.load_config(params)

    Clusterizer.load_config()
    Clusterizer.cluster()


if __name__ == 'main':
    main()
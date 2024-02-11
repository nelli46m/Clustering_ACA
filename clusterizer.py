import pandas as pd
import yaml
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, SpectralClustering, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import inspect

class Clusterizer:
    def __init__(self, path, algo, config_path=None):
        self.params = None
        self.hyperparameters = None
        self.path = path
        self.algo = algo
        self.config_path = config_path
        self.X = None

    def load_data(self):
        df = pd.read_csv(self.path)
        self.X = df.values

    def load_config(self, given_params=None):
        if self.config_path:
            with open(self.config_path, 'r') as file:
                self.params = yaml.safe_load(file)
        elif given_params:
            self.params = {}
            if given_params.hyperparameters:
                for i in range(0, len(given_params.hyperparameters), 2):
                    name = given_params.hyperparameters[i]
                    value = given_params.hyperparameters[i + 1]
                    self.params[name] = value

    def cluster(self):
        if self.algo == 'all' and self.config_path:
            for algo, params in self.params.items():
                self.cluster_with_algo(algo, params)
        else:
            self.cluster_with_algo(self.algo, self.params)

    def cluster_with_algo(self, algo, params):
        if algo == 'KMeans':
            model = KMeans(**params)
        elif algo == 'Spectral':
            model = SpectralClustering(**params)
        elif algo == 'Agglomerative':
            model = AgglomerativeClustering(**params)
        elif algo == 'DBSCAN':
            model = DBSCAN(**params)
        elif algo == 'GMM':
            model = GaussianMixture(**params)
        else:
            raise ValueError(f"Unknown algorithm: {algo}")

        self.hyperparameters = [*inspect.getfullargspec(model.__init__).args[1:]]
        self.hyperparameters += inspect.getfullargspec(model.__init__).kwonlyargs

        labels = model.predict(self.X)
        silhouette = silhouette_score(self.X, labels)
        print(f"Silhouette Score for {algo}: {silhouette}")

        self.plot_clusters(algo, labels)

    def plot_clusters(self, algo, labels):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.X[:, 0], self.X[:, 1], c=labels, cmap='viridis')
        plt.title(f'Clusters by {algo}')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.colorbar(label='Cluster')
        plt.savefig(f'{algo}_clusters.png')
        plt.close()

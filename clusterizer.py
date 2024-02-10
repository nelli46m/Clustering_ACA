import pandas as pd
import yaml
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, SpectralClustering, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

class Clusterizer:
    def __init__(self, data, algo, config_path=None):
        self.data = data
        self.algo = algo
        self.config_path = config_path
        self.load_data()
        self.load_config()
        self.cluster()

    def load_data(self):
        self.df = pd.read_csv(self.data)
        self.X = self.df.values

    def load_config(self):
        if self.config_path:
            with open(self.config_path, 'r') as file:
                self.config = yaml.safe_load(file)

    def cluster(self):
        if self.algo == 'all' and self.config_path:
            for algo, params in self.config.items():
                self.cluster_with_algo(algo, params)
        else:
            self.cluster_with_algo(self.algo, self.config)

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

import inspect
from sklearn.cluster import KMeans, DBSCAN

model = KMeans
hyperparameters = [*inspect.getfullargspec(model.__init__).args[1:]]
hyperparameters += inspect.getfullargspec(model.__init__).kwonlyargs
print(hyperparameters)

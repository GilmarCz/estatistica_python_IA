from sklearn.cluster import KMeans
import numpy as np

HorasEstudo = [1,2,3,4,5,6,7,8,9]
Nota = [35,45,50,60,65,70,80,85,95]

X = np.array(list(zip(HorasEstudo, Nota)))

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

print(kmeans.labels_)  # <- aqui o algoritmo gera os clusters sozinho
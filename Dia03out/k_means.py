import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dados fictícios
df = pd.DataFrame({
    'HorasEstudo': [1,2,3,4,5,6,7,8,9],
    'Nota': [35,45,50,60,65,70,80,85,95]
})

X = df[['HorasEstudo', 'Nota']]

# Modelo com 3 grupos
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)
print(df)

import matplotlib.pyplot as plt

# Dados
HorasEstudo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Nota = [35, 45, 50, 60, 65, 70, 80, 85, 95]
Cluster = [2, 2, 2, 0, 0, 0, 1, 1, 1]

# Plot
plt.figure(figsize=(8,5))
scatter = plt.scatter(HorasEstudo, Nota, c=Cluster, cmap='viridis', s=100)
plt.xlabel("Horas de Estudo")
plt.ylabel("Nota")
plt.title("Clusters K-Means de Alunos")
plt.colorbar(scatter, label='Cluster')
plt.grid(True)
plt.show()
import numpy as np

bolas = np.array(['R', 'R', 'R', 'B', 'B'])
n_sim = 10000

#Sorteia 3 bolas com reposição em cada simulação
sorteios =  np.random.choice
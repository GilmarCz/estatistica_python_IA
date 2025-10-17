import numpy as np

# Lista para array
arr = np.array([1, 2, 3, 4])
print(arr)

# Array 2D
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

# Arrays com valores automáticos
zeros = np.zeros((2, 3))
a=zeros;
print (a);
ones = np.ones((2, 3))
b=ones;
print (b);
range_array = np.arange(0, 10, 2)  # 0 a 8, passo 2
linspace_array = np.linspace(0, 1, 5)  # 5 valores entre 0 e 1
arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)   # Soma escalar
print(arr * 2)    # Multiplicação escalar
print(arr ** 2)   # Potenciação
print(np.sqrt(arr))  # Raiz quadrada
print(np.mean(arr))  # Média
print(np.sum(arr))   # Soma
print(np.std(arr))   # Desvio padrão
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])     # Primeiro elemento
print(arr[-1])    # Último elemento
print(arr[1:4])   # Slice do índice 1 até 3
print(arr[arr > 25])  # Filtro com condição
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a + b)  # Soma
print(a * b)  # Multiplicação elemento a elemento
print(np.dot(a, b))  # Produto matricial
print(a.T)  # Transposta
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# Primeiro gráfico
plt.figure()
plt.plot(x, np.sin(x))
plt.title("Seno")
plt.show(block=False)  # NÃO bloqueia o código, janela fica aberta

# Segundo gráfico
plt.figure()
plt.plot(x, np.cos(x))
plt.title("Cosseno")
plt.show(block=False)

# Terceiro gráfico
plt.figure()
plt.plot(x, np.tan(x))
plt.ylim(-10, 10)
plt.title("Tangente")
plt.show(block=False)

input("Pressione Enter para fechar tudo...")
plt.close('all')
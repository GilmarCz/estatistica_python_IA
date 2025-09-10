# Efetuar cálculo da Correlação e visualização entre horas dormidas e desempenho
import numpy as np
import matplotlib.pyplot as plt

# Horas dormidas por noite (exemplo)
horas_dormidas = np.array([4,5,6,7,8,9])
# Desempenho em um teste (notas fictícias)
desempenho = np.array([50,55,65,75,80,85])

# Cálculo da correlação de Pearson
correlacao = np.corrcoef(horas_dormidas, desempenho)[0, 1]
print(f"Coeficiente de correlação de Pearson: {correlacao:.4f}")

# Ajuste linear (reta de tendência)
coeficientes = np.polyfit(horas_dormidas, desempenho, 1)
reta_tendencia = np.poly1d(coeficientes)

# Plotagem dos dados e da reta de tendência
plt.scatter(horas_dormidas, desempenho, color='blue', label='Dados')
plt.plot(horas_dormidas, reta_tendencia(horas_dormidas), color='red', label='Reta de Tendência')
plt.xlabel('Horas Dormidas por Noite')
plt.ylabel('Desempenho no Teste')
plt.title('Correlação entre Horas Dormidas e Desempenho')
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de série temporal
datas = pd.date_range(start='2025-01-01', periods=12, freq='M')
valores = [100, 120, 130, 150, 170, 160, 180, 200, 220, 210, 230, 250]
serie = pd.Series(valores, index=datas)

# Média móvel com janela de 3 períodos
media_movel = serie.rolling(window=3).mean()

# Visualizando
plt.plot(serie, label='Original', marker='o')
plt.plot(media_movel, label='Média Móvel (3 meses)', marker='o')
plt.title('Média Móvel')
plt.xlabel('Data')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

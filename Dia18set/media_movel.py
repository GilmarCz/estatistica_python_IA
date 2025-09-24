import numpy as np
import pandas as pd
temperaturas = np.random.randint(20, 35, size=20)
df_temp = pd.DataFrame(temperaturas, columns=['Temperatura'])
df_temp['Media_Movel'] = df_temp['Temperatura'].rolling(window=3).mean()
print(df_temp)

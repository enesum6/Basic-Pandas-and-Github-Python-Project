import pandas as pd

# Örnek bir DataFrame oluşturma
data = {'column1': [1, 2, 3], 'column2': [4.5, 6.7, None], 'column3': ['a', 'b', 'c']}
df = pd.DataFrame(data)

# df.info() metodunu çağırma
df.info()

import pandas as pd
import numpy as np

data={
    "column1":[1,2,3,4,5],
    "column2":[10,20,13,45,25],
    "column3":["abc","bca","ade","cba","dea"]
}

df=pd.DataFrame(data)
print(df)
#ikinci sütundaki elemanları yazdırmak için
print(df["column2"].unique())
#ikinci sütundaki elemanların sayısını yazdırmak için
print(df["column2"].nunique())
#sütunları sıralamak için
print(df.columns)
print(len(df.columns))
print(df.index)
print(len(df.index))
#column1 sütununu sıralamak için
print(df.sort_values("column1"))
#column2 sütununu sıralamak için
print(df.sort_values("column2"))
#column3 sütununu sıralamak için
print(df.sort_values("column3"))
#column3 sütununu tersten sıralamak için
print(df.sort_values("column3",ascending=False))



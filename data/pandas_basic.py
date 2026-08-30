import pandas as pd

df = pd.read_csv("programs.csv")

print(df.head())
print("数据规模:", df.shape)
print("字段名称:", list(df.columns))
df.info()
import pandas as pd

df = pd.read_csv("data/programs.csv")

print(df.head())       # 查看前5行
print(df.shape)        # 查看行数和列数
print(df.columns)      # 查看列名
print(df.info())       # 查看数据类型和缺失情况
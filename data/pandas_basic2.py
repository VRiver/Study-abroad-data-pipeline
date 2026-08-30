import pandas as pd

df = pd.read_csv("programs.csv")

print("缺失值统计：")
print(df.isna().sum())  # 查看缺失值情况   

print("重复行数量：")
print(df.duplicated().sum())  # 查看重复行数量

print("重复记录：")
print(df[df.duplicated()])  # 查看重复记录
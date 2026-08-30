import pandas as pd

df = pd.read_csv("programs.csv")
# 标准化国家名称
df["country"] = df["country"].replace({
    "USA": "United States",
    "US": "United States"
})

print("数据规模:", df.shape)
print("缺失值统计：")
print(df.isna().sum())  # 查看缺失值情况

#根据school、program、degree查找重复项目
duplicates = df[
    df.duplicated(
        subset=["school", "program", "degree"],
        keep=False
    )
]
print("重复记录：")
print(duplicates)  # 查看重复记录

# 获取各列缺失值统计，转换为字典格式
missing_counts = df.isna().sum().to_dict()

duplicate_rows = df[
    df.duplicated(
        subset=["school", "program", "degree"],
        keep=False
    )
]

duplicate_count = len(duplicate_rows)

print("数据质量报告")
print("=" * 30)
print("总行数：", len(df))
print("总列数：", len(df.columns))
print("缺失值统计：", missing_counts)
print("重复记录数：", duplicate_count)

if duplicate_count > 0:
    print("质量提醒：发现重复项目")
else:
    print("质量提醒：未发现重复项目")
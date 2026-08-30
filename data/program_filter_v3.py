import pandas as pd


# 1. 读取原始数据
df = pd.read_csv(
    r"D:\Codex项目\数据岗位冲刺\data\programs.csv"
)


# 2. 标准化国家名称
df["country"] = df["country"].replace({
    "USA": "United States",
    "US": "United States"
})


# 3. 提取 IELTS 最低分
df["ielts_min"] = df["ielts_text"].str.extract(
    r"(?i)IELTS\s*(\d(?:\.\d)?)",
    expand=False
).astype(float)


# 4. 提取学费金额
df["tuition_amount"] = (
    df["tuition_text"]
    .str.extract(r"([\d,]+)", expand=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)


# 5. 提取货币
df["currency_raw"] = df["tuition_text"].str.extract(
    r"([$A-Z]+)",
    expand=False
)

df["currency"] = df["currency_raw"].replace({
    "$": "USD"
})


# 6. 提取支付周期
df["tuition_period"] = df["tuition_text"].str.extract(
    r"(?i)(year|semester|term|program)",
    expand=False
)


# 7. 设置用户需求
user = {
    "target_countries": ["United States", "Canada"],
    "degree": "Master",
    "budget": 40000,
    "ielts": 6.5
}


# 8. 分别判断每个条件是否满足
df["country_match"] = df["country"].isin(
    user["target_countries"]
)

df["degree_match"] = (
    df["degree"] == user["degree"]
)

df["tuition_match"] = (
    df["tuition_amount"] <= user["budget"]
)

df["ielts_match"] = (
    df["ielts_min"] <= user["ielts"]
)

required_columns = [
    "country",
    "degree",
    "tuition_amount",
    "ielts_min"
]

df["missing_required"] = (
    df[required_columns]
    .isna()
    .any(axis=1)
)

print(df[[
    "school",
    "program",
    "country",
    "degree",
    "tuition_amount",
    "ielts_min",
    "missing_required"
]])
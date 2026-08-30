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

missing_required = (
    df[required_columns]
    .isna()
    .any(axis=1)
)
# 单个判断成立——字段不为空且不匹配，返回1，说明不符合要求
# 多个中只要成立一个，就算显式不符合要求
explicit_mismatch = (
    (df["country"].notna()
     & ~df["country_match"])
    |
    (df["degree"].notna()
     & ~df["degree_match"])
    |
    (df["tuition_amount"].notna()
     & ~df["tuition_match"])
    |
    (df["ielts_min"].notna()
     & ~df["ielts_match"])
)

df["missing_required"] = missing_required
df["explicit_mismatch"] = explicit_mismatch

df["status"] = "待核验"

# 9. 根据缺失和显式不匹配的情况，设置状态
df.loc[
    explicit_mismatch,
    "status"
] = "不符合要求"
# 全部条件满足，且没有缺失和显式不匹配，标记为“符合要求”
df.loc[
    ~missing_required & ~explicit_mismatch,
    "status"
] = "符合要求"

status_priority = {
    "符合要求": 1,
    "待核验": 2,
    "不符合要求": 3
}

df["status_priority"] = df["status"].map(
    status_priority
)

ranked = df.sort_values(
    by=["status_priority", "tuition_amount"],
    ascending=[True, True],
    na_position="last"
)

print(ranked[[
    "school",
    "program",
    "tuition_amount",
    "currency",
    "status",
    "status_priority"
]])
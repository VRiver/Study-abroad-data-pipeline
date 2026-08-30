import pandas as pd


# =========================
# 1. 读取原始数据
# =========================

df = pd.read_csv(
    r"D:\Codex项目\数据岗位冲刺\data\programs.csv"
)


# =========================
# 2. 标准化国家名称
# =========================

df["country"] = df["country"].replace({
    "USA": "United States",
    "US": "United States"
})


# =========================
# 3. 提取 IELTS 最低分
# =========================

df["ielts_min"] = df["ielts_text"].str.extract(
    r"(?i)IELTS\s*(\d(?:\.\d)?)",
    expand=False
).astype(float)


# =========================
# 4. 提取学费金额
# =========================

df["tuition_amount"] = (
    df["tuition_text"]
    .str.extract(r"([\d,]+)", expand=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)


# =========================
# 5. 提取货币类型
# =========================

df["currency_raw"] = df["tuition_text"].str.extract(
    r"([$A-Z]+)",
    expand=False
)

df["currency"] = df["currency_raw"].replace({
    "$": "USD"
})


# =========================
# 6. 提取支付周期
# =========================

df["tuition_period"] = df["tuition_text"].str.extract(
    r"(?i)(year|semester|term|program)",
    expand=False
)


# =========================
# 7. 删除业务重复项目
# =========================

df = df.drop_duplicates(
    subset=["school", "program", "degree"],
    keep="first"
).reset_index(drop=True)


# =========================
# 8. 设置用户需求
# =========================

user = {
    "target_countries": [
        "United States",
        "Canada"
    ],
    "degree": "Master",
    "budget": 40000,
    "ielts": 6.5
}


# =========================
# 9. 判断每个条件是否满足
# =========================

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


# =========================
# 10. 判断关键字段是否缺失
# =========================

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


# =========================
# 11. 判断是否存在明确不匹配
# =========================

df["explicit_mismatch"] = (
    (
        df["country"].notna()
        & ~df["country_match"]
    )
    |
    (
        df["degree"].notna()
        & ~df["degree_match"]
    )
    |
    (
        df["tuition_amount"].notna()
        & ~df["tuition_match"]
    )
    |
    (
        df["ielts_min"].notna()
        & ~df["ielts_match"]
    )
)


# =========================
# 12. 生成项目状态
# =========================

# 默认状态：待核验
df["status"] = "待核验"


# 存在明确不符合条件的项目
df.loc[
    df["explicit_mismatch"],
    "status"
] = "不符合要求"


# 所有字段完整，并且所有条件都满足
df.loc[
    ~df["missing_required"]
    & ~df["explicit_mismatch"],
    "status"
] = "符合要求"


# =========================
# 13. 计算推荐分数
# =========================

df["recommend_score"] = 0


# 国家符合：40 分
df.loc[
    df["country_match"],
    "recommend_score"
] += 40


# 学位符合：20 分
df.loc[
    df["degree_match"],
    "recommend_score"
] += 20


# 学费符合预算：20 分
df.loc[
    df["tuition_match"],
    "recommend_score"
] += 20


# IELTS 满足要求：20 分
df.loc[
    df["ielts_match"],
    "recommend_score"
] += 20


# =========================
# 14. 设置状态排序优先级
# =========================

status_priority = {
    "符合要求": 1,
    "待核验": 2,
    "不符合要求": 3
}

df["status_priority"] = df["status"].map(
    status_priority
)


# =========================
# 15. 生成排序结果
# =========================

ranked = df.sort_values(
    by=[
        "status_priority",
        "recommend_score",
        "tuition_amount"
    ],
    ascending=[
        True,
        False,
        True
    ],
    na_position="last"
)


# =========================
# 16. 输出最终结果
# =========================

print("项目推荐结果：")

print(
    ranked[[
        "school",
        "program",
        "country",
        "degree",
        "tuition_amount",
        "currency",
        "tuition_period",
        "ielts_min",
        "status",
        "recommend_score"
    ]].to_string(index=False)
)


print("\n数据质量摘要：")

print(
    "项目总数：",
    len(df)
)

print(
    "符合要求：",
    (df["status"] == "符合要求").sum()
)

print(
    "待核验：",
    (df["status"] == "待核验").sum()
)

print(
    "不符合要求：",
    (df["status"] == "不符合要求").sum()
)

print(
    "关键字段缺失项目：",
    df["missing_required"].sum()
)
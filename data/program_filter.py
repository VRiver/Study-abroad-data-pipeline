import pandas as pd

df = pd.read_csv(
    r"D:\Codex项目\数据岗位冲刺\data\programs.csv"
)

df["country"] = df["country"].replace({
    "USA": "United States",
    "US": "United States"
})

df["ielts_min"] = df["ielts_text"].str.extract(
    r"(?i)IELTS\s*(\d(?:\.\d)?)",
    expand=False
).astype(float)

df["tuition_amount"] = (
    df["tuition_text"]
    .str.extract(r"([\d,]+)", expand=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

user = {
    "target_countries": ["United States", "Canada"],
    "degree": "Master",
    "budget": 40000,
    "ielts": 6.5
}

filtered = df[
    (df["country"].isin(user["target_countries"])) &
    (df["degree"] == user["degree"]) &
    (df["tuition_amount"] <= user["budget"]) &
    (df["ielts_min"] <= user["ielts"])
]

print(filtered[[
    "school",
    "country",
    "program",
    "degree",
    "tuition_amount",
    "ielts_min"
]])
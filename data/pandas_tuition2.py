import pandas as pd

df = pd.read_csv(
    r"D:\Codex项目\数据岗位冲刺\data\programs.csv"
)

df["tuition_amount"] = (
    df["tuition_text"]
    .str.extract(r"([\d,]+)", expand=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["currency_raw"] = df["tuition_text"].str.extract(
    r"([$A-Z]+)",
    expand=False
)

df["currency"] = df["currency_raw"].replace({
    "$": "USD"
})

df["tuition_period"] = df["tuition_text"].str.extract(
    r"(?i)(year|semester|term|program)",
    expand=False
)

print(df[[
    "school",
    "program",
    "tuition_text",
    "tuition_amount",
    "currency",
    "tuition_period"
]])
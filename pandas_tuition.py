import pandas as pd

df = pd.read_csv(
    r"D:\Codex项目\数据岗位冲刺\data\programs.csv"
)

df["tuition_clean_text"] = df["tuition_text"].str.extract(
    r"([\d,]+)",
    expand=False
)

df["tuition_usd"] = (
    df["tuition_clean_text"]
    .str.replace(",", "", regex=False)
    .astype(float)
)

print(df[[
    "program",
    "tuition_text",
    "tuition_clean_text",
    "tuition_usd"
]])

print(df["tuition_usd"].dtype)
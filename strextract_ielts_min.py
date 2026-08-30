import pandas as pd

df = pd.read_csv("programs.csv")

df["ielts_min"] = df["ielts_text"].str.extract(
   r"(?i)ielts\s*(\d(?:\.\d)?)",
    expand=False
)

df["ielts_min"] = df["ielts_min"].astype(float)

print(df[["program", "ielts_text", "ielts_min"]])
print(df["ielts_min"].dtype)
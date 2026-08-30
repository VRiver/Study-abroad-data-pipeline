import pandas as pd
df = pd.read_csv("programs.csv")
df["country"] = df["country"].replace({
    "USA": "United States",
    "US": "United States"
})

duplicates = df[
    df.duplicated(
        subset=["school", "program", "degree"],
        keep=False
    )
]

print("业务重复记录：")
print(duplicates)

df = df.drop_duplicates(
    subset=["school", "program", "degree"],
    keep="first"
)

print("清洗后行数：", len(df))
print(df[["school", "country", "program", "degree"]])
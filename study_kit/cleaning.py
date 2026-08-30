import re
import pandas as pd


def clean_programs(raw: pd.DataFrame) -> pd.DataFrame:
    """标准化国家/学位，抽取 IELTS 与学费，并按业务键去重。"""
    df = raw.copy()
    country_map = {"USA": "United States", "US": "United States", "United States": "United States"}
    degree_map = {"Master's": "Master", "MSc": "Master", "MS": "Master", "Bachelor's": "Bachelor"}
    df["country"] = df["country"].replace(country_map)
    df["degree"] = df["degree"].replace(degree_map)
    df["ielts_min"] = df["ielts_text"].astype("string").str.extract(r"(?i)(?:ielts\s*)(\d(?:\.\d)?)", expand=False).astype(float)
    df["tuition_usd"] = (
        df["tuition_text"].astype("string").str.replace(",", "", regex=False)
        .str.extract(r"(\d+(?:\.\d+)?)", expand=False).astype(float)
    )
    return df.drop_duplicates(subset=["school", "country", "degree"], keep="first").reset_index(drop=True)

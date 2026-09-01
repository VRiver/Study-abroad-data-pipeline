import json
from pathlib import Path

import pandas as pd


DATA_DIR = Path(r"D:/Codex项目/数据岗位冲刺/data")
JSON_PATH = DATA_DIR / "raw_pages.json"
JSONL_PATH = DATA_DIR / "raw_pages.jsonl"
CSV_PATH = DATA_DIR / "filtered_pages.csv"




def classify_page(page):
    url = page["url"].lower()
    title = page["title"].lower()
    content = page["content"].lower()

    excluded_url_keywords = [
        "/login",
        "/news",
        "/contact",
        "/privacy",
        "/error",
    ]

    for keyword in excluded_url_keywords:
        if keyword in url:
            return "exclude", f"URL包含无关页面关键词：{keyword}"

    if "login" in title:
        return "exclude", "页面标题显示为登录页"

    useful_keywords = [
        "program",
        "tuition",
        "ielts",
        "admission requirements",
        "application deadline",
    ]

    if any(keyword in content for keyword in useful_keywords):
        return "keep", "包含项目相关字段"

    return "review", "无法确认是否为项目页面"


def main():
    # 从 JSONL 读取原始页面数据，不在本程序中重新定义 pages
    pages = []
    with JSONL_PATH.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                pages.append(json.loads(line))

    results = []

    for page in pages:
        status, reason = classify_page(page)

        result = page.copy()
        result["page_status"] = status
        result["exclude_reason"] = reason
        results.append(result)

    result_df = pd.DataFrame(results)
    result_df.to_csv(
        CSV_PATH,
        index=False,
        encoding="utf-8-sig",
    )

    print("原始页面数量：", len(pages))
    print("页面分类结果：")
    print(result_df[["url", "title", "page_status", "exclude_reason"]])
    print("\n分类统计：")
    print(result_df["page_status"].value_counts())
    print("\n文件已生成：")
    print(JSON_PATH)
    print(JSONL_PATH)
    print(CSV_PATH)


if __name__ == "__main__":
    main()

import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"
all_books = []

#按循环抓取每一页的书籍信息,这个程序的关键点
for page_number in range(1, 4):
    if page_number == 1:
        page_url = BASE_URL
    else:
        page_url = urljoin(
            BASE_URL,
            f"catalogue/page-{page_number}.html"
        )

    print("正在抓取：", page_url)

    response = requests.get(
        page_url,
        timeout=10
    )

    response.raise_for_status()
    response.encoding = "utf-8"

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    book_cards = soup.find_all(
        "article",
        class_="product_pod"
    )

    for card in book_cards:
        link = card.find("h3").find("a")

        title = link.get("title")
        relative_url = link.get("href")
        full_url = urljoin(page_url, relative_url)

        price_text = card.find(
            "p",
            class_="price_color"
        ).get_text(strip=True)

        price_amount = float(
            price_text
            .replace("£", "")
        )

        book = {
            "title": title,
            "price": price_text,
            "price_amount": price_amount,
            "url": full_url,
            "page_number": page_number
        }

        all_books.append(book)


books_df = pd.DataFrame(all_books)

output_path = (
    r"D:\Codex项目\数据岗位冲刺\data"
    r"\books_pagination.csv"
)

books_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print("\n抓取完成")
print("总数据量：", books_df.shape)
print("\n每页数据量：")
print(books_df["page_number"].value_counts().sort_index())

print("\n前5条数据：")
print(books_df.head())

print("\n缺失值检查：")
print(books_df.isna().sum())

print("\n重复标题数量：")
print(books_df["title"].duplicated().sum())

print("\n文件已保存：", output_path)
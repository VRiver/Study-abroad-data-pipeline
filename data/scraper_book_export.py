import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=10)
response.raise_for_status()
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

book_cards = soup.find_all(
    "article",
    class_="product_pod"
)

books = []

#按循环读入字段信息
for card in book_cards:
    link = card.find("h3").find("a")
    relative_url = link.get("href")

    book = {
        "title": link.get("title"),
        "price": card.find(
            "p",
            class_="price_color"
        ).get_text(strip=True),
        "url": urljoin(url, relative_url)
    }

    books.append(book)

books_df = pd.DataFrame(books)

#对相关字段做提取，保存数值    
books_df["price_amount"] = (
    books_df["price"]
    .str.replace("£", "", regex=False)
    .astype(float)
)

books_df.to_csv(
    "books_scraped.csv",
    index=False,
    encoding="utf-8-sig"
)
print("数据行列：", books_df.shape)
print(books_df.head(3))
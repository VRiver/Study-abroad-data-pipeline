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

print("数据行列：", books_df.shape)
print(books_df.head(3))
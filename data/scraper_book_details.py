import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

book_cards = soup.find_all(
    "article",
    class_="product_pod"
)

books = []

for card in book_cards:
    link = card.find("h3").find("a")

    book = {
        "title": link.get("title"),
        "price": card.find(
            "p",
            class_="price_color"
        ).get_text(strip=True),
        "url": link.get("href")
    }

    books.append(book)

print("提取书籍数量：", len(books))
print("前3条书籍数据：")

for book in books[:3]:
    print(book)
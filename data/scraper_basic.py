import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=10)

response.raise_for_status()
print("网页获取成功")
print("状态码：", response.status_code)
print("网页内容长度：", len(response.text))
#print("网页前500个字符：")
#print(response.text[:500])
# with open("page.html", "w", encoding="utf-8") as file:
#     file.write(response.text)

soup = BeautifulSoup(response.text, "html.parser")

book_tags = soup.find_all("h3")

print("找到的书籍数量：", len(book_tags))
print("书名列表：")

for book_tag in book_tags:
    link = book_tag.find("a")

    visible_title = link.get_text(strip=True)
    full_title = link.get("title")

    print("页面显示标题：", visible_title)
    print("完整书名：", full_title)
    # print(book_tag.get_text(strip=True))
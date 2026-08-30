from typing import Iterable
import requests
from bs4 import BeautifulSoup


def fetch_html(url: str, timeout: int = 10) -> str:
    response = requests.get(url, timeout=timeout, headers={"User-Agent": "study-kit/1.0"})
    response.raise_for_status()
    return response.text


def extract_program_cards(html: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for card in soup.select(".program-card"):
        title = card.select_one(".title")
        country = card.select_one(".country")
        if title:
            rows.append({"program": title.get_text(" ", strip=True), "country": country.get_text(" ", strip=True) if country else ""})
    return rows

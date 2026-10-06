import requests
from bs4 import BeautifulSoup

url = "https://www.mext.go.jp/a_menu/lifescience/bioethics/seimeikagaku_igaku.html"

response = requests.get(url, timeout=30)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text("\n")

for keyword in [
    "令和8年8月27日",
    "令和7年12月26日",
    "更新しました"
]:
    pos = text.find(keyword)

    print("=" * 60)
    print(keyword)
    print("=" * 60)

    if pos != -1:
        print(text[max(0, pos-500):pos+2000])
    else:
        print("見つからない")

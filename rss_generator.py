import requests
from bs4 import BeautifulSoup

url = "https://www.mext.go.jp/a_menu/lifescience/bioethics/seimeikagaku_igaku.html"

response = requests.get(url, timeout=30)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text("\n")

lines = text.splitlines()

for line in lines:
    line = line.strip()

    if "令和8年8月27日" in line:
        print("FOUND:", line)

    if "令和7年12月26日" in line:
        print("FOUND:", line)

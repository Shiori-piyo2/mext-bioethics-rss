import requests
from bs4 import BeautifulSoup

url = "https://www.mext.go.jp/a_menu/lifescience/bioethics/seimeikagaku_igaku.html"

response = requests.get(url, timeout=30)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

lines = soup.get_text("\n").splitlines()

for line in lines:
    line = line.strip()

    if "更新しました" in line:
        print("NEWS:", line)

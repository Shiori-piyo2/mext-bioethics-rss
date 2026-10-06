import requests

html = requests.get(
    "https://www.mext.go.jp/a_menu/lifescience/bioethics/seimeikagaku_igaku.html",
    timeout=30
).text

keyword = "新着情報"

pos = html.find(keyword)

print(html[max(0, pos-1000):pos+3000])

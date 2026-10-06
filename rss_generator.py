import requests

url = "https://www.mext.go.jp/a_menu/lifescience/bioethics/seimeikagaku_igaku.html"

response = requests.get(url, timeout=30)

response.encoding = response.apparent_encoding

html = response.text

keyword = "新着情報"

pos = html.find(keyword)

print("位置:", pos)

if pos != -1:
    print(html[max(0, pos-1000):pos+3000])
else:
    print("見つからない")

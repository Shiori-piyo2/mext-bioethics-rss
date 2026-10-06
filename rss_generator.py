import requests

url = "https://www.mext.go.jp/a_menu/lifescience/bioethics/seimeikagaku_igaku.html"

response = requests.get(url, timeout=30)

response.encoding = response.apparent_encoding

html = response.text

print(html[:5000])

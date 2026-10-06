import requests

url = "https://www.mext.go.jp/a_menu/lifescience/bioethics/seimeikagaku_igaku.html"

response = requests.get(url, timeout=30)
response.encoding = response.apparent_encoding

html = response.text

for keyword in [
    "令和8年8月27日",
    "令和7年12月26日",
    "更新しました"
]:
    pos = html.find(keyword)

    print("\n")
    print("=" * 50)
    print(keyword)
    print("=" * 50)
    print("位置:", pos)

    if pos != -1:
        print(html[max(0, pos-1000):pos+3000])

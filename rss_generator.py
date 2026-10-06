import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

URL = "https://www.mext.go.jp/a_menu/lifescience/bioethics/seimeikagaku_igaku.html"

response = requests.get(URL, timeout=30)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

lines = [line.strip() for line in soup.get_text("\n").splitlines()]
lines = [line for line in lines if line]

items = []

for line in lines:
    if "更新しました" in line:
        items.append({
            "title": f"【生命科学・医学系研究】{line}",
            "link": URL
        })

fg = FeedGenerator()

fg.id(URL)
fg.title("文科省 生命科学・医学系研究 RSS")
fg.link(href=URL)
fg.description("人を対象とする生命科学・医学系研究 新着情報")

for item in items:
    fe = fg.add_entry()

    fe.id(item["title"])
    fe.title(item["title"])
    fe.link(href=item["link"])
    fe.description(item["title"])
    fe.pubDate(datetime.now(timezone.utc))

fg.rss_file("feed.xml")

print(f"RSS作成完了: {len(items)}件")

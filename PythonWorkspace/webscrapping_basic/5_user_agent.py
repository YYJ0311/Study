# user agent string 검색

import requests
res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status() # 웹 스크래핑 진행

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
# user agent string 검색

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":""} # 내 user agent
res = requests.get(url, headers=headers)
# res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
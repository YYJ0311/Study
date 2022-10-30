# pip install requests 다운로드 필요
import requests
res = requests.get("http://google.com")

print("응답코드 :", res.status_code) # 200 : 정상

if res.status_code == requests.codes.ok: # 정상이면(상태 코드가 200이면)
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status() # 웹 스크래핑 진행

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
    # 생성된 html을 open in browser를 통해 확인가능
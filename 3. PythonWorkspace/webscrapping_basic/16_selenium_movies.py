import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies?hl=ko&gl=US"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})
movies = soup.find_all("div", attrs={"class":"hP61id"})
print(len(movies))

### html 만들기
# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 정돈되게 출력

# 만약 영화정보가 제대로 불러와지지 않으면 
# 생성된 html파일 우클릭 - open in default browser 로 페이지 확인
# 접속하는 사용자의 Header 정보를 통해서 구글 무비에서 서로 다른 페이지를 리턴해주기 때문
# 한글이 제대로 안 나오면 user agent와 Accept-Language를 설정해서 한글페이지 지정

### 제목 가져오기
for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)

# 가져온 페이지 정보를 보면 모든 정보를 보여주지 않음
# 스크롤을 하게 되면 생기는 페이지도 가져오기 위해 selenium 사용
# pip install beautifulsoup4
# pip install lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # text를 lxml parser를 통해서 beautifulsoup 객체 생성
print(soup.title) # <title>네이버 웹툰 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text()) # 네이버 웹툰 > 요일별  웹툰 > 전체웹툰
print(soup.a) # <a href="#menu" onclick="document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"><span>메인 메뉴로 바로가기</span></a>
# soup => 첫번째로 발견되는 정보를 보여줌
print(soup.a.attrs) # attrs = 가지고 있는 속성, {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}
print(soup.a["href"]) # #menu

print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class가 Nbtn_upload인 a 태그 찾기. <a class="Nbtn_upload" href="/mypage/myActivity" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
print(soup.find(attrs={"class":"Nbtn_upload"})) # Nbtn_upload 클래스가 하나면 옆 코드처럼 사용가능

print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a) # <a href="/webtoon/detail?titleId=783053&amp;no=53" onclick="nclk_v2(event,'rnk*p.cont','783053','1')" title="김부장-53화 그게 뭔지 아세요?">김부장-53화 그게 뭔지 아세요?</a>
# soup을 통해 발견한 객체를 다시 soup 객체와 같이 다룸. a태그만 가져옴
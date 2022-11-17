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

print(rank1.a.get_text()) # 1위 웹툰 text만
print(rank1.next_sibling) # 아무것도 안 나옴. 순위 사이에 줄바꿈 때문
print(rank1.next_sibling.next_sibling) # 2위 웹툰 정보 출력

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling # previous로 이전 항목 가져올 수 있음
print(rank2.a.get_text())

print(rank1.parent) # ol 태그 출력됨
rank2 = rank1.find_next_sibling("li") # 조건(li)에 해당하는 것만 찾음
print(rank2.a.get_text()) # 중간의 줄바꿈 신경쓰지 않고 바로 출력할 수 있음
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

print(rank1.find_next_siblings("li")) # 다음 li들을 모두 가져옴

webtoon = soup.find("a", text="내 남편과 결혼해줘-53화") # text에 해당하는 a태그를 가져옴
print(webtoon)
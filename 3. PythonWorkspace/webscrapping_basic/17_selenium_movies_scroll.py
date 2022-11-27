from selenium import webdriver

# def selenium():
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies?hl=ko&gl=US"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 1920 x 1080에서 해상도만큼 스크롤 내림

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 현재 문서의 높이만큼 스크롤을 내림

# 스크롤 내리는 것을 반복해서 가장 마지막 페이지까지 가기 (구글무비 옛날 페이지는 스크롤로 목록을 계속 로드하는 형식이었음)
import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 내려온 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height # prev_height 업데이트

print("스크롤 완료")

# 스크래핑
# 모든 영화 정보를 가져옴
import requests
from bs4 import BeautifulSoup

print(browser.page_source)
soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})
movies = soup.find_all("div", attrs={"class":"hP61id"})
# 클래스 명 여러개 가져오기 => 리스트 [] 사용
# movies = soup.find_all("div", attrs={"class":["VfPpkd-EScbFb-JIbuQc UVEnyf", "추가 검색할 클래스"]})

print(len(movies)) # 스크롤을 내려서 전체 제목을 가져왔기 때문에 그 양이 16번에서 구한 것 보다 더 많다.

### 제목 가져오기
for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()

    # 할인 전 가격정보(할인이 들어간 항목들)
    original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
    if original_price: # 할인전 가격이 있으면 정보 가져옴
        original_price = original_price.get_text()
    else:
        print(title, " <할인되지 않은 영화 제외>")
        continue

    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()

    # 링크정보
    # link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    # 올바른 링크 : https://play.google.com + link
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    # print(f"링크 : ", "https://play.google.com" + link)
    print("-" * 100)

    
    # # selenium 창 유지
    # while(True): 
    #     pass

# selenium()
# 최근 5년간 연도별 역대 관객순위 1~5위 영화 포스터를 자동으로 다운로드하는 스크래핑 프로그램 만들기
import requests
from bs4 import BeautifulSoup

for year in range(2017, 2022): # 2017~2021
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"]) # src부분을 가져옴
        image_url = image["src"]
        if image_url.startswith("//"): # https가 없는 경로에 붙여줌
            image_url = "https:" + image_url
        
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status # 접근 확인

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f: # jpg 형태로 제공되고 있어서 선택함
            f.write(image_res.content) # content = 이미지

        if idx >= 4: # 상위 5개의 이미지까지만 다운로드
            break
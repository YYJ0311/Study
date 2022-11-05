# 네이버 "코스피 시가총액 순위" 상위 200개를 csv 파일로 저장하기
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # 자동 줄바꿈을 공백으로(디폴트 줄바꿈을 없앰)
# encoding을 utf8로만 쓰면 생성된 파일을 확인했을 때 한글이 깨져있음. utf-8-sig 으로 사용하면 됨.
writer = csv.writer(f) # 이걸 이용해서 파일 씀

# csv 상단에 제목 입력
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

for page in range(1, 5): # 1 ~ 4페이지
    res = requests.get(url + str(page))
    res.raise_for_status() # 문제 없는지 확인
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)
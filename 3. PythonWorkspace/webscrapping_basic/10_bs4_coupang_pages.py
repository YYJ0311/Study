import requests
import re
from bs4 import BeautifulSoup

##### 쿠팡은 이 방법으로 크롤링 안 됨

headers = {"User-Agent":""}

for i in range(1, 6): # 1페이지부터 5페이지까지 반복
    # url의 page에 i 넣음
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # li 태그 중에서 class 정보가 search-product로 시작하는 모든 element를 가져옴

    for item in items:
        # 광고 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
        # 애플 제품 제외
        if "Apple" in name:
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
        
        # 리뷰 100개 이상, 평점 4.5 이상되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"}) # 평점
        if rate: # rate가 있으면
            rate = rate.get_text()
        else:
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1] # 1번째 부터 뒤에서 1번째 까지
        else:
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"] # 링크정보

        if float(rate) >= 4.5 and int(rate_cnt) >= 100: # rate를 실수로 변환, rate_cnt를 int로 변환
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) # 줄 긋기
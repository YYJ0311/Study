from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
time.sleep(0.5) # 너무 빨리 실행되면 오류가 발생해서 실행 1초 늦춤..

#   이번달 3일, 6일 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/button").click()
time.sleep(0.5)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/button").click()
# xpath말고 다른 요소로 선택을 해서 다른 월, 일을 선택하는 방법도 생각해보기

time.sleep(0.5)

# 인기 여행지 버튼의 두번째 항목 선택
browser.find_elements(By.CSS_SELECTOR, "button.Popular_button__3LeIb")[1].click()
time.sleep(0.5)

# 항공권 검색 클릭. 도착지를 선택해야 사용 가능.
# browser.find_element(By.CSS_SELECTOR, "button.searchBox_search__2KFn3").click()

# 선택한 여행지 비행 스케줄의 세번째 일정 선택하기
browser.find_elements(By.CLASS_NAME, "recommend_item__1W_5a")[2].click()
# time.sleep(500)
    # 여기서 아래 항공편 출력으로 바로 넘어가면 중간 로딩 화면때문에 xpath를 바로 찾을 수 없음
    # 따라서 element가 나올 때까지만 기다리게 도와주는 것들(By, WebDriverWait, expected_conditions)을 import하고 사용함

# time.sleep(15)
# browser.find_element(By.CSS_SELECTOR, "div[class='concurrent_inner__iqfJr']").click()
# time.sleep(500)

time.sleep(20)
    # 항공편 페이지가 국제선, 국내선으로 나눠져서 페이지가 달라지기 때문에 아래에서 태그를 기다리는 기능으로는 아직 구현하지 못하겠음. 그래서 20초 기다리게 만듦..
try:
    # 국제선 div class : international_content__2Z9HD
    # 국내선 div class : domestic_flight_content__ZPRcn

    if browser.find_element(By.CLASS_NAME, "international_content__2Z9HD").is_displayed :
        elem = WebDriverWait(browser, 500).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='concurrent_inner__iqfJr']"))) 
        # ()안의 태그 element가 나올때까지 500초 동안 기다림
    elif browser.find_element(By.CLASS_NAME, "domestic_flight_content__ZPRcn").is_displayed :
        elem = WebDriverWait(browser, 500).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='domestic_Flight__sK0eA']")))
        ##### 국내선 정보 가져오는 부분에서 list가 제대로 생성되지 않아 오류나옴. 수정 필요*****

    # 전체 티켓정보를 리스트에 저장한 뒤 출력할 예정
        # class나 css_selector로 불러와서 출력하기 위해 text 함수를 사용하려 했는데...
        # 해당 메소드는 Webelement 인스턴스여야만 사용할 수 있음
        # 따라서 list를 생성해서 넣어주고 원하는 것만 불러올 것임
    ticket_list = []
    for i in elem:
        ticket_list.append(i.text)
        print(ticket_list)
finally:
    print(elem[0].text) # 첫번째 항공편 텍스트 정보 출력
    # browser.quit() # 오류 여부와 상관없이 브라우저 종료
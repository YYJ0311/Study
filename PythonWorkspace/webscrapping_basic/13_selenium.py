# pip install selenium

# chromedriver
    # 크롬에서 chrome://version 으로 버전정보 확인 : 107.0.5304.88
    # 구글에서 chromedriver 검색 후 chromium 사이트 접속
    # 내 버전과 맞는 것을 다운로드하기(운영체제 확인)
    # 압축해제해서 우리가 사용하고자 하는 폴더(PythonWorkspace)에 exe 파일 넣기

from selenium import webdriver

browser = webdriver.Chrome() # 다른 경로에 exe파일이 있는 경우 () 안에 ""로 경로 적어주기
browser.get("http://naver.com")

# TERMINAL에서 python을 인터프리터 형식으로 실행하여 위 코드 입력
# 이후 띄워진 웹에서 우리가 원하는 것들을 찾아서 실행 가능함

# from selenium.webdriver.common.by import By
    # By 를 import
# elem = browser.find_element(By.CLASS_NAME, "link_login")
# elem
    # elem 값 확인
# elem.click()
    # 로그인 버튼이 클릭됨
# 다음의 명령어로 페이지 이동/새로고침 가능
    # browser.back()
    # browser.forward()
    # browser.refresh
# browser.back()
    # 초기화면으로 돌아옴
# elem = browser.find_element(By.ID, "query")
    # 검색창 id 저장
# from selenium.webdriver.common.keys import Keys
    # Keys.ENTER를 사용하기 위해 Keys를 import 함
# elem.send_keys("키 입력하기")
# elem.send_keys(Keys.ENTER)
    # 엔터를 누름으로써 검색실행
# elem = browser.find_element(By.TAG_NAME, "a")
    # elem으로 확인해보면 a 태그 하나만 가져옴
# elem = browser.find_elements(By.TAG_NAME, "a")
    # elements로 모든 a 태그를 불러올 수도 있음
# for e in elem:
#    e.get_attribute("href")
    # 인터프리터에 입력할 때 tab으로 꼭 띄워주기! 그리고 엔터 한 번 더 누르기
# browser.get("http://daum.net")
    # 페이지 이동
# elem = browser.find_element(By.NAME, "q")
    # 다음의 검색창 선택
# elem.send_keys("다음 검색")
# elem.send_keys(Keys.ENTER)
# browser.back()
# elem = browser.find_element(By.NAME, "q")
# elem.send_keys("다음 검색")

# 검색 버튼 클릭을 xpath로 실행하기
    # 버튼 태그 확인, 우클릭해서 xpath copy
# elem = browser.find_element(By.XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[3]")
    # @id 뒤의 ""를 ''로 변경
# elem
# elem.click()
    # xpath로 불러온 클릭 버튼이 클릭됨

# browser.close()
    # 현재 탭만 종료
# browser.quit()
    # 브라우저 전체 종료

# exit()
    # python 인터프리터 종료
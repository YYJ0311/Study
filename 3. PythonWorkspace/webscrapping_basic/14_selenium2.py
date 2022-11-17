from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome() # 다른 경로에 exe파일이 있는 경우 () 안에 ""로 경로 적어주기

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("naver_id")
browser.find_element(By.ID, "pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

time.sleep(3) # 3초 대기

# 5. id 새로 입력
browser.find_element(By.ID, "id").clear() # 입력된 id 지우기
browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit()
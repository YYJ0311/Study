```
웹 스크래핑
    웹페이지에서 필요한 부분만 가져오는 것

웹 크롤링
    웹 페이지 내 허용된 링크들을 따라가며 모든 내용을 가져오는 것

HTML (Hyper Text Markup Language) 사용
    TechER의 open in browser vsc extension 설치

    w3school 참고

user agent
    구글에 user agen string 검색
    https://www.whatismybrowser.com/detect/what-is-my-user-agent/

    접속하는 브라우저에 따라 user agent가 달라짐
    서버는 user agent 를 확인해서 정보를 다르게 보여줄 수 있음

beautifulsoup4
    스크래핑을 하기 위해 사용되는 패키지

lxml
    구문을 분석하는 parser

selenium에서 element를 찾기위해 By 사용하기
    from selenium.webdriver.common.by import By

    driver.find_element(By.XPATH, '//button[text()="Some text"]')
    driver.find_element(By.XPATH, '//button')
    driver.find_element(By.ID, 'loginForm')
    driver.find_element(By.LINK_TEXT, 'Continue')
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
    driver.find_element(By.NAME, 'username')
    driver.find_element(By.TAG_NAME, 'h1')
    driver.find_element(By.CLASS_NAME, 'content')
    driver.find_element(By.CSS_SELECTOR, 'p.content')

    driver.find_elements(By.ID, 'loginForm')
    driver.find_elements(By.CLASS_NAME, 'content')
```
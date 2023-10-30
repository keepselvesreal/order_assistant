from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def login_to_website():
    site = "https://www.instagram.com/"
    driver = webdriver.Chrome()
    driver.get(site)
    
    # 로그인 버튼 찾기 (XPath 사용) | ts-아래처럼 기다리는 처리하지 않아 오류 발생했음
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[.//div[text()="로그인"]]')))

    # username 입력 필드 찾기
    username_field = driver.find_element(by="name", value="username")
    password_field = driver.find_element(by="name", value="password")

    # username 필드에 값 입력하기
    id = 'keep_selves_real'
    password = 'kts71611089!'

    username_field.send_keys(id)
    password_field.send_keys(password)

    # 로그인 버튼 클릭하기
    login_button.click()

    # '나중에 하기' 버튼 찾기 (XPath 사용)
    later_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@role="button" and text()="나중에 하기"]')))

    # '나중에 하기' 버튼 클릭하기
    later_button.click()

    # 알림 설정 나중에 버튼 클릭하기

def hello_world():
    print("Hello World!")
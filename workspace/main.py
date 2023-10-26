from orderbot import split_conversation, save_prev_conversation, order

# 웹스크래핑 코드

# 모듈화 할 부분
new_message_windows = get_new_message_windows():
   
# 
if new_message_windows:
    for new_message_window in new_message_windows:
        new_message_window.click()
        
        # 대화 내용이 로드될 때까지 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, others_msg_selector))
        )
        
        # 현재 페이지의 HTML을 가져와서 파싱
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # 가장 최근 날짜와 대화 내용 추출
        recent_date = soup.select(date_selector)[-1].text
        conversation
        if not first_conversation:
            prev_conversation, customer_query = split_conversation(conversation)
            save_prev_conversation(prev_conversation)
        
            
            
            
        
        
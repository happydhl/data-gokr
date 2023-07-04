# python -m venv myenv  가상 환경
# .\myenv\Scripts\activate  시행 에러 나오면 Power shell 권한 실행 후 Executionpolycy 실행 
# pip install pandas, selenium, lxml    자료 정제 후 CSV, 엑셀에 사용 하기 위한 퍀케이지 설치
#selenium 사용 하기 위해 크롬 드라이버 chromediriver 검색후 본인 버젼(chrome://version)  해야 함
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

# 조회 항목 초기화
checkboxes = browser.find_elements(By.NAME,'fieldIds')
for checkbox in checkboxes: 
    if checkbox.is_selected(): #체크상태라면? 
        checkbox.click() #클릭 (체크.해제)

# 조회 항목을 체크 (원하는 항목)
items_to_select = ['영업이익','자산총계' ,'매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH,'..')
    label = parent.find_element(By.TAG_NAME,'label')
    #print(label.text) # 이름을 확인 
    if label.text in items_to_select: # 선택 항목
        checkbox.click() # 체크

# 적용하기 클릭

btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

# 5. 데이터 추출
for idx in range(1,43): # 40미만 페이지 반복
    # 사전 작업 : 페이지 이동
    browser.get(url + str(idx)) # http://naver.com....&page=2
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True) # 전체 자료 없으면(결측치) 지우라...any는 한 자료라도 없으면
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:
        break

    # 6. 파일 저장

    f_name = 'sise.csv'
    if os.path.exists(f_name): # 파일이 있다면 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a',header=False)
    else:
        df.to_csv(f_name, encoding='utf-8-sig', index=False)

    print(f'{idx} 페이지 완료')

browser.quit()

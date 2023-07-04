from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("./chromedriver.exe", options=chrome_options)
# browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME,"link_login")
elem.click()
browser.back()
elem = browser.find_element(By.ID,"query")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
elem = browser.find_elements(By.TAG_NAME,"a")
for e in elem:
    e.get_attribute("href")

browser.get("http://daum.net")
elem = browser.find_elements(By.ID_NAME,"q")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
elem = browser.find_elements(By.XPATH,"//*[@id='daumSearch']/fieldset/div/div/button[3]")
print(elem)
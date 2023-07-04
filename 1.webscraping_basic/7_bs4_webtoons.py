# pip install beautifulsoup4  스크래핑 하기위한
# pip install lxml   구분을 분석 parser 
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# 네이버 웹툰 전체 목록 가져옥;
cartoons = soup.find_all("a", attrs={"class":"alt"})
# class 속성이 title 인 모든 "a" element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())

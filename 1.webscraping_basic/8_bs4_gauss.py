# pip install beautifulsoup4  스크래핑 하기위한
# pip install lxml   구분을 분석 parser 
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/bestChallenge"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://commin=c.naver.com" + link)

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)

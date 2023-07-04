# pip install beautifulsoup4  스크래핑 하기위한
# pip install lxml   구분을 분석 parser 
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
#print(soup.a) #soup 객체이서 처음 발견 되는 a element 를 츨력
#print(soup.a.attrs) # a element 의 속성 값을 출력
#print(soup.a["href"]) # a element의 href 속성 값 정보를 출력

# print(soup.find("div", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload"인 a element를 찾아줘
# print(soup.find(attrs={"class":"u_skip"})) # class="Nbtn_upload"인  어떤 element를 찾아줘
# print(soup.find("li",attrs={"class":"rank01"})) 
#rank1 = soup.find("li", attrs={"class":"rank01"})
# #print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
#print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="김부장")
print(webtoon)
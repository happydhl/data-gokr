import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1,11): #2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i)) # 파일로 저정 1~10.png
    time.sleep(2) # 2초 단위


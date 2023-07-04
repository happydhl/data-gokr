from random import *
from math import *

# users = range(1,21)
# print(users,type(users))
# users = list(users)
# print(users,type(users))
# shuffle(users)
# print(users,type(users))
# lst =sample(users,4)
# print(" 1 등 {0}".format(lst[0]))
# print(" 2~3 등 {0}".format(lst[1:4]))

# weather = input("오늘 날씨 어때?")
# if weather == "비" :
#     print("우산 챙기삼")
# elif weather == "미세먼지" :
#     print("마스크 챙기감")
# else :
#     print("준비물 필요 없음")

# starbucks = ["이이언맨", "토르", "앙그루"]
# for customer in starbucks:
#     print(" {0}.., 커피 드세요.".format(customer))

# absent = [2,5]
# no_book = [7]
# for student in range(1,11) :
#     if student in absent: 
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0}는 교무실로".format(student))
#         break
#     print("{0}, 씨 책을 읽어줘".format(student))

# student = ["ion man", "tore " ,"adsdafasdf"]
# student = [i.upper() for i in student]
# print(student)

# cnt = 0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15 :
#         print("[0] {0} 번쨰 손님 ( 소요시간 {1} 분 ".format(i, time))
#         cnt +=1
#     else:
#          print("[ ] {0} 번쨰 손님 ( 소요시간 {1} 분 ".format(i, time))

# print(" 총 탑승 승갹 : {0}".format(cnt))
#
#  함수
# def profile(name, age, *languge):
#     print("이름 : {0} \t 나이  {1} \t ".format(name,age), end=" ")
#     for lang in languge:
#         print(lang, end=" ")
#     print()
# profile("유재석", 20, "python", "java", "c", "c++")
# profile("김태로", 25, "python", "java")

# def std_weight(height, gender):
#     std_w = 0
#     if (gender == "남자") :
#          return pow(height,2) *22
#     else :
#         return pow(height,2) *21
  
# height = 172
# gender = "남자"
# weigth = round(std_weight(height / 100, gender),2)
# print(" 키 {0} \t 성별 {0}".format(height,gender), end=" ")
# print(" 키 {0} 남자의 표준 체중은 {1}".format(height, weigth))

# 입출력
# scores = {"수학":0, "영어" : 50, "코딩": 100}
# for subject, score in scores.items():
#       print(subject.ljust(8), str(score).rjust(4), sep=":")
# print("{0:+,}".format(100000000000))
# print("{0:.2f}".format(5/3))

#입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
# score_file= open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 90")
# score_file.write("\n코딩 : 90")
# score_file.close()
# score_file = open("score.txt", "r", encoding="utf8")
# # print(score_file.read())
# while True:
#     line = score_file.readline()
#     if not line: break
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line,end="")
# score_file.close()

# pickle

import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수", "나이":30 , "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file)) # close 할 필요 없이 2줄로 끝

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이슨을 열심히 공부 하고 있네요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# CLASS  편
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name =name         #class 정의 멤버 변수 
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
    
# marine1= Unit("말린", 40, 50)
# marine2= Unit("말린", 40, 50)
# tank = Unit("탱크", 150,35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛이름 {0}, 공격력 {1}".format(wraith1.name,wraith1.damage))

# wraith2 = Unit("레이스", 80, 5)
# wraith2.clockking = true  #외부에서 class 변수룰 추가로 설정 가능 하다

#메소드
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name =name         #class 정의 멤버 변수 
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
#     def attack(self, location):
#         print("{0} : {1} 빙향으로 적군을 공격합니다. [공격력{2}]"\
#               .format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{0}  : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재체력은 {1}".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} 죽었습니다".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# #공격 2 받는
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속
# class Unit:
#     def __init__(self, name, hp):
#         self.name =name         #class 정의 멤버 변수 
#         self.hp = hp
        
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self,name,hp)
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
#     def attack(self, location):
#         print("{0} : {1} 빙향으로 적군을 공격합니다. [공격력{2}]"\
#               .format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{0}  : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재체력은 {1}".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} 죽었습니다".format(self.name))

# # 드립쉽 : 공중 유닛,수송기,마린/파이어뱃/텡크 등을 수송, 공격 x
#  날수 있는 기능 을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print(" {0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
#               .format(name, location, self.flying_speed))
# 다중 상속 설명  공중, 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self,name, hp, damage)
#         Flyable.__init__(self,flying_speed)

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


# 오버라이딩  위에 다중 상속 확장 하여 설명
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name =name        
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동 합니다. 속도 {2}"\
#               .format(self.name,location,self.speed))

        
# class AttackUnit(Unit):
#     def __init__(self, name, hp,speed, damage):
#         Unit.__init__(self,name,hp,speed)
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
#     def attack(self, location):
#         print("{0} : {1} 빙향으로 적군을 공격합니다. [공격력{2}]"\
#               .format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{0}  : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재체력은 {1}".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} 죽었습니다".format(self.name))

# # 드립쉽 : 공중 유닛,수송기,마린/파이어뱃/텡크 등을 수송, 공격 x
# #날수 있는 기능 을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print(" {0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
#               .format(name, location, self.flying_speed))

# 공중, 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self,name, hp, 0, damage) # attack 은 지상 나는 스피드 없으므로 0
#         Flyable.__init__(self,flying_speed)
# # 개선 추가 하는 코딩
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80 , 10, 20)
# # 배틀클루져 : 공중 유닛, 체력도 굉장히 좋은, 공격력도 좋음
# battlecruser = FlyableAttackUnit("배틀크루져", 500,25,3)
# vulture.move("11시")
# #battlecruser.fly(battlecruser.name,"9시")  # 공격 과 플라잉 구분 하여 move, fly 하는 어려윰
# battlecruser.move("9시")  # 다중 오버라이드 fly ==> move 로 통일 하는 방법
# # 즉 Unit 에 move 함수를 FlyableAttckUnit 에 move 함수를 재 정의 하여 개선 한 것임

# # PASS 
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass  # 아무일 안하고 지나감
# # 서플라이 디폿 : 건물, 1개 건물 - 8유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# # SUPER 
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#        #Unit.__init__(self,name,hp,speed)
#        super().__init__(name,hp,speed)  # super() 쓰고, self) 안쓴다
# # 서플라이 디폿 : 건물, 1개 건물 - 8유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# # 스티크래프트 작성
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name =name        
#         self.hp = hp
#         self.speed = speed
#         print(" {0} 유닛이 생성 되었습니다".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동 합니다. 속도 {2}"\
#               .format(self.name,location,self.speed))
#     def damaged(self, damage):
#         print("{0}  : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재체력은 {1}".format(self.name, self.hp))
#         if self.hp <= 0 :
#            print("{0} 죽었습니다".format(self.name))
        
# class AttackUnit(Unit):
#     def __init__(self, name, hp,speed, damage):
#         Unit.__init__(self,name,hp,speed)
#         self.damage = damage
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
#     def attack(self, location):
#         print("{0} : {1} 빙향으로 적군을 공격합니다. [공격력{2}]"\
#               .format(self.name, location, self.damage))
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
        
#     def fly(self, name, location):
#         print(" {0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
#               .format(name, location, self.flying_speed))        
# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
#     # 스팀팩 : 일정시간 동안 이동, 공격력 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다.(hp 10감소)".format(self.name))
#         else:
#             print("{0} : 체력 부족으로 스팀팩 사용 못함".format(self.name))
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정 시켜, 파워 증가
#     seize_developed = False #씨즈모드 개발 여부
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크",150 , 1, 15)
#         self.seize_mode = False
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#            return
#         # 현재 시즈모드가 아닐 때 - >시즈모드    
#         if self.seize_mode == False:
#             print(" {0} : 시즈모드로 전환 합니다".format(self.name))
#             self.damage *= 2
#             self.set_seize_mode = True
#         else:
#             print(" {0} : 시즈모드로 해제 합니다".format(self.name))
#             self.damage /= 2
#             self.set_seize_mode = False

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self,name, hp, 0, damage) # attack 은 지상 나는 스피드 없으므로 0
#         Flyable.__init__(self,flying_speed)
# # 개선 추가 하는 코딩
#     def move(self, location):
#        self.fly(self.name, location)    

# #레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스",80,20, 5)
#         self.clocked = False  # 클러크 모드 (해제 상태)
#     def clocking(self):
#         if self.clocked == True:
#             print(" {0} : 클로킹 모드 해제 합니다".format(self.name))
#             self.clocked = False
#         else:
#             print(" {0} : 클로킹 모드 설정 합니다".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작 합니다")
# def game_over():
#     print(" Player GG")
#     print("[Player]이 게임에서 퇴장하셨습니다")

# # rp임 진행
# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank() 
# t2 = Tank() 

# w1 = Wraith()
# # 유닛 일관 관리 리스트
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈 모드 개발
# Tank.seize_developed = True
# print("[알림] 텡크 시즈 모드 개발이 완료 되었습니다")

# # 공격모드 준비(마린 : 스팀팩 텡크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해  
# for unit in attack_units:
#     unit.damaged(randint(5,21)) # 공격은 래덤으로

# #게임졸료
# game_over()

# 예외 처리
# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg
    
# try:
#     print(" 한자리 숫자 나누기 계산기.")
#     num1 = int(input(" 첫번째 숫자 ? :"))
#     num2 = int(input(" 주번째 숫자 ? :"))
#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError(" 입력값 : {0}, {1}".format(num1,num2))
#     print("{0}, / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력 한 자리 숫자 요 함")
# except BigNumberError as err:
#     print("에러가 발생... 한 자리 숫자 요 함")
#     print(err)
#  finally:
#     print(" 계산기 이용 감사")
       
# 모듈
# import theater_module
# theater_module.price(3) # 3명 일반
# theater_module.price_morning(4) # 4명 조조 할인
# theater_module.price_soldier(5) # 5명 군인

# import theater_module as mv # 모듈명 길때 별명 사용
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)
# from theater_module import price, price_morning  # 필요한 모듈만 호출 할 수 있음
# mv.price_soldier(5)  # 에러가 남
# from theater_module import price_soldier as price  # 군인만 호출  arias  price로 사용

# 펙키지  여러 모듈을 모은 것
# import travel.thailand  # import 여기에는 모듈이나 펙케이지만 가능 하다. CLASS,함수 쓰면 오류
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage  # from 에서는 CLASS 사용 가능 하다
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#from random import *  # 이전 사용 했긋이..
# from travel import *
# trip_to = vietnam.VietnamPackage() # 맨처음 에러 나옴  __init__ 안에 공개 범위 설정 필요 함
# trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 모듈 직접 실행
# 모듈이나 팩키지 개발시 직접 테스트 해 보는 방법을 제시 하는 것 

# 모듈이나 팩키지 실행 위치를 확인 하는 방법( 지금은 같은 디랙토리에 있었고..)

# import inspect
# import random
# print(inspect.getfile(random))   # C:\Python311\Lib\random.py  이라 나옴

# from travel import *
# print(inspect.getfile(thailand)) 
# c:\Users\UserK\Desktop\pythonworkspace\travel\thailand.py  이전
# C:\Python311\Lib\travel\thailand.py travel 디랙토리 이동 후 다시 실행 후 

# PIP INSTALL    구글에서 PYPI 에서 여러 형태 검색 해 볼것!  beautifulsoup
# pip install beautifulsoup4  copy 실행창에서 실행 하면 자동 down 수행 됨
# PIP LIST 하면 설치된석 나옴 / pip show beatifulsoup4 치면 해당 정보 보여 줌
# pip install --upgrade beautifulsoup4 하면 최신으로 UPDATE 함
# pip uninstall beautifulsoup4
# 에제 프로그램 3줄 copy 
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장 함수
# print 같은 기본 내장 함수
# print(dir())
# import pickle
# print(dir())  # 추가 되어 pickle 이 보임
# print(dir(random))  # randim 안에 함수를 볼 수 있다

# lst = [1,2,3]
# print(dir(lst))
# name = "lee duk"
# print(dir(name))

# 외장 함수  구글 list uf python modules   치면 나옴 
# glob  : 경로 내의 폴더 /화일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디랙토리

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다")
#     os.rmdir(folder)
#     print(folder," 폴더를 삭제 하였습니다")
# else:
#     os.makedirs(folder)  #폴더 생성
#     print(folder,"폴더를 생성 하였습니다")
# print(os.listdir())

# import time  # 시간 관련 외장 함수 
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# #timedelta : 두 날짜 사잉의 간격
# today = datetime.date.today() #오늘 날짜
# td = datetime.timedelta(days=100)
# print("우리 만난지 100일은", today + td) # 오늘 부터 100일 후

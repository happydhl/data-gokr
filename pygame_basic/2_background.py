import pygame

pygame.init()  #초기화 반드시 필요
#화면 크기
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("이덕행 첫 게임") # 게임 이름
#배경 이미지
background = pygame.image.load("C:/Users/UserK/Desktop/pythonworkspace/pygame_basic/backgroud.png")


#이벤트 루프
running = True # 게임이 진행 중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생 하였는가?
            running = False
    #screen.fill(0,0,255))  # 직접 칼라 입력
    screen.blit(background, (0,0))  #배경 그리기
    pygame.display.update() #게임 화면을 다시 그리기

pygame.quit() #게임 종료
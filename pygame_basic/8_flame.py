#프레임 만들기
import pygame
#################################################
#기본 초기화 (반드시 해야 하는 것들)
pygame.init()  #초기화 반드시 필요
#화면 크기
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("이덕행 첫 게임") # 게임 이름

#FPS
clock = pygame.time.Clock()
#################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

#이벤트 루프
running = True 
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수를 선정
    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        
    #3. 게임 캐릭터 위치 정의    
    
    
    #4. 충돌 처리를 위한 rect 정보 업데이트
    
    #5. 화면에 그리기
    #screen.fill(0,0,255))  # 직접 칼라 입력

    pygame.display.update() #게임 화면을 다시 그리기 무조건 실행
pygame.quit() #게임 종료
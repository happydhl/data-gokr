import pygame

pygame.init()  #초기화 반드시 필요
#화면 크기
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("이덕행 첫 게임") # 게임 이름

#FPS
clock = pygame.time.Clock()


#배경 이미지
background = pygame.image.load("C:/Users/UserK/Desktop/pythonworkspace/pygame_basic/backgroud.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/UserK/Desktop/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #세로 크기
character_x_pos = screen_width / 2 - character_width/2  #화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height  #화면 세로 크기 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0
# 이동 속도 추가
character_speed = 0.3

#이벤트 루프
running = True # 게임이 진행 중인가?
while running:
    dt = clock.tick(20) #게임 화면의 초당 프레임 수를 선정
    #케릭터가 1초 동안에 100만큼 이동을 해야 함
    #10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동 ? 10 * 10 = 100
    #20 fps 는 1번에 5만 큼  5*20 = 100이므로

    for event in pygame.event.get(): #어떤 이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생 하였는가?
            running = False
        
        if event.type == pygame.KEYDOWN : #키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP: #캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: 
                to_y += character_speed
        if event.type == pygame.KEYUP : # 방향키를 쩨면 멈춤
            if event.key == pygame.K_LEFT or pygame.K_RIGHT: 
                to_x = 0
            elif event.key == pygame.K_UP or pygame.K_DOWN: 
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #screen.fill(0,0,255))  # 직접 칼라 입력
    screen.blit(background, (0,0))  #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos) ) # 캐릭터 그리기
    pygame.display.update() #게임 화면을 다시 그리기

pygame.quit() #게임 종료
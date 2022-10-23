import pygame
from random import *
#######################################################
# 기본 초기화 (반드시 해야 하는 것)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("falling poop")

# FPS
clock = pygame.time.Clock()
#######################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경화면
background = pygame.image.load("C:\\Users\\Joon\\Desktop\\Practice\\Study\\PythonWorkspace\\pygame_quiz\\background.png")

# 캐릭터
character = pygame.image.load("C:\\Users\\Joon\\Desktop\\Practice\\Study\\PythonWorkspace\\pygame_quiz\\man_left.png")
character_size = character.get_rect().size # 사이즈 지정
character_width = character_size[0] # 0번째 값 = width
character_height = character_size[1] # 1번째 값 = height
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - 10 # 잔디 위에 캐릭터 위치
character_speed = 0.6

# 이동할 좌표
to_x = 0
# to_y = 0

# 똥
poop = pygame.image.load("C:\\Users\\Joon\\Desktop\\Practice\\Study\\PythonWorkspace\\pygame_quiz\\poop.png")
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = randrange(0, screen_width - poop_width) # 똥의 x좌표. 0부터 (스크린 너비 - 똥 너비)까지 랜덤
# poop_x_pos = randint(0, screen_width - poop_width) # randint로도 사용 가능
poop_y_pos = 0 # 초기 y좌표
poop_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 100

# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        # type이 quit이면 실행 종료
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 키보드를 눌렀을 때
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
                character = pygame.image.load("C:\\Users\\Joon\\Desktop\\Practice\\Study\\PythonWorkspace\\pygame_quiz\\man_left.png")
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
                character = pygame.image.load("C:\\Users\\Joon\\Desktop\\Practice\\Study\\PythonWorkspace\\pygame_quiz\\man_right.png")

        if event.type == pygame.KEYUP: # 키보드에서 뗐을 때. 설정을 안 하면 눌렀을 때의 입력값이 계속 반복된다.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터의 위치 정의
    character_x_pos += to_x * dt
    # character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # poop 위치 정의
    poop_y_pos += poop_speed

    if poop_y_pos > screen_height: # == 을 쓰면 작동 안 됨
        poop_y_pos = 0
        poop_x_pos = randrange(0, screen_width - poop_width)

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos

    # 충돌 체크
    if character_rect.colliderect(poop_rect):
        print("충돌했어요")
        running = False    

    # 화면에 표시
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    screen.blit(poop, (poop_x_pos, poop_y_pos))

    # 타이머 넣기, 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과시간을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 남은 시간. 밀리세컨드를 자르기 위해 int 타입 사용. 다시 string으로 바꿔서 문자형으로 사용. 출력할 글자/True/글자색상
    screen.blit(timer, (10, 10))
        # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        pygame.time.delay(1000)
        running = False

    pygame.display.update()

# pygame 종료
pygame.quit()
import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Test Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\Joon\\Desktop\\Practice\\Study\\PythonWorkspace\\pygame_basic\\background.png")

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((0, 0, 255)) # rgb 값으로 배경 그리기
    screen.blit(background, (0, 0)) # 좌측상단이 0, 0. 배경 그리기
    pygame.display.update() # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()
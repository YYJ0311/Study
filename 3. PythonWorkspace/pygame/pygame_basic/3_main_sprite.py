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

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\Joon\\Desktop\\Practice\\Study\\PythonWorkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size # rectangle. 이미지의 크기를 구해옴
character_width = character_size[0] # 첫번째 값. 가로
character_height = character_size[1] # 두번째 값. 세로
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에서 캐릭터의 절반 크기만큼 더 이동해야 함
character_y_pos = screen_height - character_height # 화면 세로 크기의 가장 아래에서 캐릭터의 크기만큼 올라와야 함

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()


# pygame 종료
pygame.quit()
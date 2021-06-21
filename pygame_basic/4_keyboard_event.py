import pygame

pygame.init() #초기화
#화면 크기 설정

screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

#배경이미지 불러오기
background=pygame.image.load("C:/Users/jeung/OneDrive/문서/test/pygame_basic/backgroun.png")

#캐릭터 불러오기
character=pygame.image.load("C:/Users/jeung/OneDrive/문서/test/pygame_basic/character.png")
character_size=character.get_rect().size
character_widht=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2 - character_widht/2
character_y_pos=screen_height-character_height

#이동할 좌표
to_x=0
to_y=0

#이벤트 루프

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x-=1
            elif event.key==pygame.K_RIGHT:
                to_x+=1
            elif event.key==pygame.K_UP:
                to_y-=1
            elif event.key==pygame.K_DOWN:
                to_y+=1

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0

    character_x_pos+=to_x
    character_y_pos+=to_y

    #가로 경계값 처리
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_widht:
        character_x_pos=screen_width-character_widht
    #세로 경계값 처리
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height




    screen.blit(background,(0,0)) #배경그리기
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()
    
#pygame 종료
pygame.quit()


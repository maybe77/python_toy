import pygame
import random
import timeit


'''
    초기값 설정

'''
pygame.init()
screen_width=480
screen_height=960
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("avoid collision")


clock=pygame.time.Clock()

background=pygame.image.load("C:/Users/jeung/OneDrive/문서/test/pygame_basic/backgroun.png")

character=pygame.image.load("C:/Users/jeung/OneDrive/문서/test/pygame_basic/character.png")
character_size=character.get_rect().size
character_height=character_size[1]
character_width=character_size[0]
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-character_height

class enemy:
    def __init__(self,x_pos,speed):
        self.enemy_=pygame.image.load("C:/Users/jeung/OneDrive/문서/test/pygame_basic/enemy.png")
#        self.enemy_.enemy_size=self.enemy_.get_rect().size
        self.enemy_height=self.enemy_.get_height()
        self.enemy_width=self.enemy_.get_width()
        self.enemy_x_pos=x_pos
        self.enemy_y_pos=0
        self.enemy_speed=speed
        self.enemy_delete=0
        print("장애물이 생성되었습니다.")
    
    def falling(self):
        self.enemy_y_pos+=self.enemy_speed
        

    def __del__(self):
        print("1")



to_x=0
to_y=0
character_speed=0.5
score=0
game_font=pygame.font.Font(None,40)
times=timeit.default_timer()
start_time=pygame.time.get_ticks()
prev_time=0
enemy_num=0
create_enemy=[]
live_enemy=[]
delete_param=0
delete_flag=0
dead_enemy=[]
score=0


'''
    게임구동
'''

running = True
while running:
    dt=clock.tick(120)
    
    # 캐릭터 이동
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y-=character_speed
            elif event.key == pygame.K_DOWN:
                to_y+=character_speed
            elif event.key == pygame.K_RIGHT:
                to_x+=character_speed
            elif event.key == pygame.K_LEFT:
                to_x-=character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0

    character_x_pos+=to_x*dt
    character_y_pos+=to_y*dt


    #가로 경계값 처리
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
    #세로 경계값 처리
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height


    # 장애물 생성
    if pygame.time.get_ticks()/1000-prev_time>2:
        prev_time=pygame.time.get_ticks()/1000
        enemy_x_pos=random.randrange(0,450,50)
        enemy_y_speed=random.uniform(0.5,1)

        create_enemy.append(enemy(enemy_x_pos,enemy_y_speed))
        live_enemy.append(enemy_num)
        print(create_enemy[enemy_num].enemy_x_pos,create_enemy[enemy_num].enemy_y_pos,create_enemy[enemy_num].enemy_height,create_enemy[enemy_num].enemy_width)
        enemy_num+=1


    #장애물 하강
    for i in range(len(live_enemy)):
        create_enemy[i].falling()

    #장애물 소멸
    for i in range(len(live_enemy)):
        if create_enemy[i].enemy_y_pos>950 and create_enemy[i].enemy_delete==0:
            create_enemy[i].enemy_delete=1
            score+=100
            print("장애물이 파괴되었습니다")
#    live_enemy=live_enemy - dead_enemy
        
#        del create_enemy[delete_param]    
#        live_enemy=list(x for x in live_enemy if x not in dead_enemy)

    #캐릭터 좌표
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    #장애물 좌표
    for i in range(len(live_enemy)):            
        enemy_rect=create_enemy[i].enemy_.get_rect()
        enemy_rect.left=create_enemy[i].enemy_x_pos
        enemy_rect.top=create_enemy[i].enemy_y_pos


        #충돌체크
        if character_rect.colliderect(enemy_rect):
            print("충돌했어요")
            running=False


    screen.blit(background,(0,0)) #배경그리기
    screen.blit(character,(character_x_pos,character_y_pos))

    #장애물 그리기
    for i in range(len(live_enemy)):
        screen.blit(create_enemy[i].enemy_,(create_enemy[i].enemy_x_pos,create_enemy[i].enemy_y_pos))

    elapsed_time=(pygame.time.get_ticks() - start_time)/1000
    time=game_font.render(str(int(elapsed_time)),True,(255,255,255))
    scores=game_font.render(str(int(score)),True,(255,255,255))
    screen.blit(time,(10,10))
    screen.blit(scores,(400,10))
    
    pygame.display.update()
    
pygame.time.delay(2000)

#pygame 종료
pygame.quit()

    





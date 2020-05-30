"""
事件操作：
发生的事情
存放事件的列表
Eventlist = pygame.event.get()

键盘
key.get_pressed()
"""
#导入游戏模块
import pygame,sys


pygame.init()

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

bg1_x = 0
bg1_y = 0

bg2_x = 0
bg2_y = -SCREEN_HEIGHT

#英雄飞机初始位置
hero_x = (SCREEN_WIDTH-114)//2
hero_y = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)


background_image1 = pygame.image.load("images/bg/bg5.jpg")
background_image2 = pygame.image.load("images/bg/bg5.jpg")
hero = pygame.image.load("images/hero/hero4.png")

clock = pygame.time.Clock()

while True:
    clock.tick(24)
    screen.blit(background_image1,(bg1_x,bg1_y))
    screen.blit(background_image2,(bg2_x,bg2_y))
    screen.blit(hero,(hero_x,hero_y))

    #获取事件
    e_list = pygame.event.get()
    #判断事件是否存在
    if len(e_list)>0:
        #事件存在
        for e in e_list:
            #获得具体事件
            if e.type == pygame.QUIT:
                #关闭游戏资源
                pygame.quit()
                sys.exit()
            # if e.type == pygame.KEYDOWN:
            #     if e.key == pygame.K_UP:
            #         print("向上运动")
            #         hero_y -= 3
            #     if e.key == pygame.K_DOWN:
            #         print("向下运动")
            #         hero_y += 3
            #     if e.key == pygame.K_LEFT:
            #         print("向左")
            #         hero_x -= 3
            #     if e.key == pygame.K_RIGHT:
            #         print("右")
            #         hero_x += 3

    #获得键盘的操作事件
    e_key = pygame.key.get_pressed()
    #要对按下按键类型进行判断
    if e_key[pygame.K_w]:
        print("上")
        hero_y -= 5
    if e_key[pygame.K_s]:
        print("下")
        hero_y += 5
    if e_key[pygame.K_a]:
        print("左")
        hero_x -= 5
    if e_key[pygame.K_d]:
        print("右")
        hero_x += 5

    #进行边界判断 三目/三元
    # if hero_x <0:
    #     hero_x = 0
    hero_x = 0 if hero_x < 0 else hero_x
    hero_x = SCREEN_WIDTH - 114 if hero_x > SCREEN_WIDTH -114 else hero_x
    hero_y = 0 if hero_y < 0 else hero_y
    hero_y = SCREEN_HEIGHT - 93 if hero_y > SCREEN_HEIGHT-93 else hero_y


    bg1_y += 5
    if bg1_y > SCREEN_HEIGHT:
        bg1_y = -SCREEN_HEIGHT
    bg2_y += 5
    if bg2_y > SCREEN_HEIGHT:
        bg2_y = -SCREEN_HEIGHT

    pygame.display.update()










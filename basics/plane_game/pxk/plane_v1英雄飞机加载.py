"""
事件操作：
发生的事情
存放事件的列表
Eventlist = pygame.event.get()
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

hero_x = (SCREEN_WIDTH-114)//2
hero_y = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
print(screen,type(screen))

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
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    print("向上运动")
                    hero_y -= 3
                if e.key == pygame.K_DOWN:
                    print("向下运动")
                    hero_y += 3
                if e.key == pygame.K_LEFT:
                    print("向左")
                    hero_x -= 3
                if e.key == pygame.K_RIGHT:
                    print("右")
                    hero_x += 3


    bg1_y += 5
    if bg1_y > SCREEN_HEIGHT:
        bg1_y = -SCREEN_HEIGHT
    bg2_y += 5
    if bg2_y > SCREEN_HEIGHT:
        bg2_y = -SCREEN_HEIGHT

    pygame.display.update()










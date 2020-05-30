#导入游戏模块
import pygame
#初始化游戏数据
pygame.init()

#不常改变的变量，一般设置为常量
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

#图片的坐标位置
bg_x = 0
bg_y = 0

bg2_x = 0
bg2_y = -768
#搭建窗口
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)

#加载背景图片
background_image1 = pygame.image.load("images/bg/bg5.jpg")
background_image2 = pygame.image.load("images/bg/bg5.jpg")

#pygame.time.Clock() 控制图片每秒播放的帧数 24/s
clock = pygame.time.Clock()

#展示更新数据
while True:
    #通过clock控制图片每秒播放的帧数
    clock.tick(24)

    #将图片渲染到游戏窗口中
    screen.blit(background_image1,(bg_x,bg_y))
    screen.blit(background_image2,(bg2_x,bg2_y))

    #让图片进行运动
    bg_y += 3
    if bg_y > SCREEN_HEIGHT:
        bg_y = -SCREEN_HEIGHT
    bg2_y += 3
    if bg2_y > SCREEN_HEIGHT:
        bg2_y = -SCREEN_HEIGHT

    pygame.display.update()

#关闭资源
pygame.quit()






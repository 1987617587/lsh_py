#导入游戏模块
import pygame
#初始化游戏数据
pygame.init()

#搭建窗口
screen = pygame.display.set_mode((512,768),0,32)

#加载背景图片
background_image = pygame.image.load("images/bg/bg5.jpg")

#展示更新数据
while True:
    #将图片渲染到游戏窗口中
    screen.blit(background_image,(0,0))

    pygame.display.update()

#关闭资源
pygame.quit()






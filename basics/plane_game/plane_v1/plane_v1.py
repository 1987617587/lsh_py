"""
# author Liu shi hao
# date: 2019/11/25 16:21
# file_name: plane_v1

"""

# 导入游戏模块
import random
import sys

import pygame

# 初始化游戏数据
from datetime import date

pygame.init()

class BaseBullet(object):
    # '''子弹类'''

    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
class Bullet(BaseBullet):
    # '''玩家子弹'''

    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 40, y - 20, '../images/bg/bullet_1.png')

    def move(self):
        self.y -= random.randint(80, 200)

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
# 把不常改变的变量，设置为常量
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

# 图片的坐标位置
bg1_x = 0  # 背景一
bg1_y = 0

bg2_x = 0  # 背景二
bg2_y = -SCREEN_HEIGHT

hero_x = (SCREEN_WIDTH - 114) // 2  # 英雄战机初始位置坐标
hero_y = 400

enemy_x = random.randint(100, 300)  # 敌方战机初始位置坐标
enemy_y = random.randint(0, 10)
# 搭建窗口
screen = pygame.display.set_mode((512, 768), 0, 32)

# 加载背景图片
background_image1 = pygame.image.load("../images/bg/bg4.jpg")
background_image2 = pygame.image.load("../images/bg/bg4.jpg")
# 加载英雄飞机图片
hero_image = pygame.image.load("../images/hero/hero3.png")

# 飞机发射子弹

# 加载敌方飞机

# 生成敌方小型飞机
small_enemies = pygame.image.load("../images/enemy/plane_s1.png")

# 生成敌方中型飞机
mid_enemies = pygame.image.load("../images/enemy/plane_s2.png")

# 生成敌方大型飞机
big_enemies = pygame.image.load("../images/enemy/plane_s3.png")


def enemy_plan():
    if random.randint(1, 60) == 6:
        screen.blit(small_enemies, (enemy_x, enemy_y + bg1_y))
    if random.randint(1, 600) == 6:
        screen.blit(mid_enemies, (enemy_x, enemy_y + bg1_y))
    if random.randint(1, 1000) == 6:
        screen.blit(big_enemies, (enemy_x, enemy_y + bg1_y))


# pygame.time.Clock() 控制图片每秒播放的帧数 24/s
clock = pygame.time.Clock()

# 加载音乐
pygame.mixer.music.load("../music/7029.mp3")
pygame.mixer.music.load("../music/7789.mp3")
pygame.mixer.music.load("../music/8226.wav")
pygame.mixer.music.load("../music/bg_music.mp3")
# pygame.mixer.music.play(-1)

# 展示更新数据
i = 0
while True:
    # 通过clock控制图片每秒播放的帧数
    clock.tick(24)

    # 将图片渲染到游戏窗口中
    screen.blit(background_image1, (bg1_x, bg1_y))
    screen.blit(background_image2, (bg2_x, bg2_y + bg1_y))
    screen.blit(hero_image, (hero_x, hero_y))
    # hero_image.Bullet(hero_image.screen, hero_x, hero_y)
    i += 1
    if i < 200:
        screen.blit(small_enemies, (enemy_x - 100, enemy_y + bg1_y))
        screen.blit(small_enemies, (enemy_x, enemy_y + bg1_y - 500))
        screen.blit(small_enemies, (enemy_x + 100, enemy_y + bg1_y))
    if 300 < i < 500:
        screen.blit(mid_enemies, (enemy_x, enemy_y + bg1_y))
    if 700 < i < 900:
        screen.blit(big_enemies, (enemy_x, enemy_y + bg1_y))
    # enemy_plan()
    if i > 1000:
        i = 0
        print(pygame.mixer.music.get_endevent)
        # break
    # 让图片动起来
    bg1_y += 3
    if bg1_y > SCREEN_HEIGHT:
        bg1_y = 0
    # 获取事件
    e_list = pygame.event.get()
    # 获得键盘的操作事件
    e_key = pygame.key.get_pressed()
    # 对要按下按键类型进行判断
    if e_key[pygame.K_UP] or e_key[pygame.K_w]:
        print("向上运动")
        hero_y -= 5
    if e_key[pygame.K_DOWN] or e_key[pygame.K_s]:
        print("向下运动")
        hero_y += 5
    if e_key[pygame.K_LEFT] or e_key[pygame.K_a]:
        print("向左运动")
        hero_x -= 5
    if e_key[pygame.K_RIGHT] or e_key[pygame.K_d]:
        print("向右运动")
        hero_x += 5
    if e_key[pygame.K_0]:
        pygame.mixer.music.play(2)

    # 判断事件是否存在
    if len(e_list) > 0:
        for e in e_list:
            # 获得具体事件
            if e.type == pygame.QUIT:
                # 关闭游戏资源
                pygame.quit()
                sys.exit()
    # 进行边界判断 三目/三元
    # if hero_x <0:
    #     hero_x = 0
    hero_x = 0 if hero_x < 0 else hero_x
    hero_x = SCREEN_WIDTH - 131 if hero_x > SCREEN_WIDTH - 131 else hero_x
    hero_y = 0 if hero_y < 0 else hero_y
    hero_y = SCREEN_HEIGHT - 105 if hero_y > SCREEN_HEIGHT - 105 else hero_y
    pygame.display.update()
# 关闭资源
# pygame.quit()

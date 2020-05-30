"""
# author Liu shi hao
# date: 2019/11/26 19:47
# file_name: task

"""
# 1.面向过程
# planev1~v5练习熟练
import pygame

pygame.init()

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

bg_x = 0
bg_y = 0

bg2_x = 0
bg2_y = -768

hero_x = (SCREEN_WIDTH-114)//2
hero_y = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
background_image1 = pygame.image.load("images/bg/bg5.jpg")
background_image2 = pygame.image.load("images/bg/bg5.jpg")
hero = pygame.image.load("images/hero/hero4.png")
clock = pygame.time.Clock()

while True:
    clock.tick(24)

    screen.blit(background_image1,(bg_x,bg_y))
    screen.blit(background_image2,(bg_x,bg_y))
    screen.blit(hero,(hero_x,hero_y))
    bg_y += 3
    if bg_y > SCREEN_HEIGHT:
        bg_y = -SCREEN_HEIGHT
    bg2_y += 3
    if bg2_y > SCREEN_HEIGHT:
        bg2_y = -SCREEN_HEIGHT

    pygame.display.update()


pygame.quit()

# 2.面向对象
# planev1~v3练习熟练
import  pygame,sys

pygame.init()

pygame.mixer.music.load("sound/gameMusic.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("飞机大战")

logo = pygame.image.load("logo.png")

pygame.display.set_icon(logo)

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768
class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image,speed):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed
    def move(self):
        print("移动了")

    def event(self):
        print("发生事件了")
        # 获取所有事件
        e_list = pygame.event.get()
        # 判断事件是否存在
        if len(e_list) > 0:
            # 对事件进行遍历循环
            for e in e_list:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    def update(self):
        self.move()
        self.event()

class BackgroundImageSprite(GameSprite):
    def move(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -SCREEN_HEIGHT

background_image1 = BackgroundImageSprite("images/bg/bg5.jpg", 5)
background_image2 = BackgroundImageSprite("images/bg/bg5.jpg", 5)
background_image2.rect.y = -SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
resource = pygame.sprite.Group(background_image1, background_image2)
clock = pygame.time.Clock()
while True:
    clock.tick(24)
    # 精灵组调用每个精灵的update方法
    resource.update()
    # 精灵组将所有精灵渲染到游戏窗口中
    resource.draw(screen)

    pygame.display.update()
# 3.功能扩展
# 控制子弹的发射频率
# 实现三孔发射
# 导入模块
import pygame as pygame
import random
import pygame
import sys

pygame.init()

# 加载音乐
pygame.mixer.music.load("music/big_eye.mp3")
# 播放音乐
pygame.mixer.music.play(-1)
# 设置标题
pygame.display.set_caption("飞机大战")

logo = pygame.image.load("images/logo.png")
# 设置图标
pygame.display.set_icon(logo)

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

hero_x = 113
hero_y = 77

# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏基类
    """

    def __init__(self, image, speed=1):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def move(self):
        # self.rect.y += self.speed
        pass

    def event(self):
        e_list = pygame.event.get()
        if len(e_list) > 0:
            for e in e_list:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def update(self):
        self.event()
        self.move()


class BackGround(GameSprite):
    """
    背景
    """

    def move(self):
        self.rect.y += self.speed
        # 判断是否移出屏幕，如果移出屏幕，将设置到屏幕的上方
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -SCREEN_HEIGHT


class PlayerPlane(GameSprite):
    """
    玩家飞机类
    """

    def __init__(self, image, speed=2):
        super().__init__(image, speed)
        self.hp = 100
        self.atk = 10
        self.rect.x = (SCREEN_WIDTH - hero_x) // 2
        self.rect.y = (2 * SCREEN_HEIGHT - hero_y) // 3
        self.bullets = pygame.sprite.Group()

    def move(self):
        # 获得键盘的操作事件
        e_key = pygame.key.get_pressed()
        # 对要按下按键类型进行判断
        if e_key[pygame.K_UP] or e_key[pygame.K_w]:
            print("向上运动")
            self.rect.y -= 5
        if e_key[pygame.K_DOWN] or e_key[pygame.K_s]:
            print("向下运动")
            self.rect.y += 5
        if e_key[pygame.K_LEFT] or e_key[pygame.K_a]:
            print("向左运动")
            self.rect.x -= 5
        if e_key[pygame.K_RIGHT] or e_key[pygame.K_d]:
            print("向右运动")
            self.rect.x += 5
        self.rect.x = 0 if self.rect.x < 0 else self.rect.x
        self.rect.x = SCREEN_WIDTH - 131 if self.rect.x > SCREEN_WIDTH - 131 else self.rect.x
        self.rect.y = 0 if self.rect.y < 0 else self.rect.y
        self.rect.y = SCREEN_HEIGHT - 105 if self.rect.y > SCREEN_HEIGHT - 105 else self.rect.y

    def fire(self):
        # 获得键盘的操作事件
        e_key = pygame.key.get_pressed()
        # 对要按下按键类型进行判断


        if e_key[pygame.K_k] or e_key[pygame.K_0]:
            print("开火")
            i = 0

            # 1.创建子弹精灵
            bullet = PlayerBullet(image="images/bullet/bullet_1.png", speed=8)
            bullet2 = PlayerBullet(image="images/bullet/bullet_1.png", speed=8)
            bullet3 = PlayerBullet(image="images/bullet/bullet_1.png", speed=8)
            # 2.设置精灵的位置
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - random.randint(0, 50)
            bullet2.rect.centerx = self.rect.centerx - 30
            bullet2.rect.bottom = self.rect.y - random.randint(0, 50)
            bullet3.rect.centerx = self.rect.centerx + 30
            bullet3.rect.bottom = self.rect.y - random.randint(0, 50)
            # 3.将精灵添加到精灵组
            self.bullets.add(bullet, bullet2, bullet3)


class EnemyPlane(GameSprite):
    """
    敌机飞机类
    """

    def __init__(self, image, speed=10):
        super().__init__(image, speed)
        self.direction = 'right'  # 定义敌机默认往右移动
        self.enemy_bullets = pygame.sprite.Group()

    def update(self):
        pass
        # # 让敌机沿垂直方向飞行
        # self.rect.y += self.speed
        # # 判断敌机是否飞出屏幕
        # if self.rect.y > SCREEN_HEIGHT:
        #     self.kill()

    def move(self):
        if self.direction == 'right':
            self.rect.x += 8
        elif self.direction == 'left':
            self.rect.x -= 8
        if self.rect.x > 270:
            self.direction = 'left'
        elif self.rect.x < 0:
            self.direction = 'right'

    def fire(self):
        # 发射子弹
        random_num = random.randint(1, 20)
        if random_num == 10 or random_num == 15:
            # 1.创建子弹精灵
            bullet = PlayerBullet(image="images/bullet/b2.png", speed=-8)
            # 2.设置精灵的位置
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - random.randint(0, 50)
            # 3.将精灵添加到精灵组
            self.enemy_bullets.add(bullet)


class Bullet(GameSprite):
    """
    子弹类
    """

    def __init__(self, image, speed):
        super().__init__(image, speed)

    def update(self):
        # 让子弹沿垂直方向飞行
        self.rect.y -= self.speed
        # 判断子弹是否飞出屏幕
        if self.rect.y < -self.rect.height or self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.kill()


class PlayerBullet(Bullet):
    """
    玩家子弹类
    """


class EnemyBullet(Bullet):
    """
    敌机子弹类
    """
    pass


background_image1 = BackGround("images/bg/bg5.jpg")
background_image2 = BackGround("images/bg/bg5.jpg")
hero_image = PlayerPlane("images/hero/hero1.png")
enemy_image = EnemyPlane("images/enemy/boss2.png")
# 设置背景图2的y值
background_image2.rect.y = -SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
# 创建一个精灵组
resource = pygame.sprite.Group(background_image1, background_image2, hero_image)
# 创建敌机精灵组
enemy_resourc = pygame.sprite.Group(enemy_image)
# 控制每秒播放帧数
clock = pygame.time.Clock()

while True:
    clock.tick(24)
    # 精灵组调用每个精灵的update方法
    resource.update()
    # 精灵组将所有精灵渲染到游戏窗口中
    resource.draw(screen)
    hero_image.move()
    hero_image.fire()

    hero_image.bullets.update()
    hero_image.bullets.draw(screen)

    enemy_resourc.update()
    enemy_resourc.draw(screen)
    enemy_image.move()

    enemy_image.enemy_bullets.update()
    enemy_image.enemy_bullets.draw(screen)
    enemy_image.fire()

    pygame.display.update()

# 4.总结pygame的API
# 加载音乐
# pygame.mixer.music,load()
# 播放音乐
# pygame.mixer.music.play(播放几遍，最高6边，-1是循环播放)
# 设置标题
# pygame.display.set_caption("标题名字")
# 设置图标
# pygame.display.set_icon(loge = pygame.image.load(图片))
# 加载图片pygame.image.load(图片)
# 获取事件(退出游戏，键盘事件pygame.K_UP...)
# e_list = pygame.event.get()
# if len(e_list)>0:
#     for e in e_list:
#         if e.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
# 创建精灵组
# resource = pygame.sprite.Group(放入多个精灵)
# 精灵组调用每个精灵的updat方法resource。update
# 精灵组将所有精灵渲染到游戏窗口中resource.draw(screen)
# 展示更新所有的数据pygame.display.update()


















































































































































# 5.开发敌方飞机类
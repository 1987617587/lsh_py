"""
# author Liu shi hao
# date: 2019/11/26 11:19
# file_name: game

"""
# 导入模块
import time

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
                    exit()
                if e.type == ENEMY_SMALL_PLANE:
                    enemy_small = EnemyPlane(list_small_enemy[random.randint(0, 4)], 8)
                    enemy_resourc.add(enemy_small)
                    print("产生小飞机")
                if e.type == ENEMY_MIDDLE_PLANE:
                    enemy_mid = EnemyPlane(list_middle_enemy[random.randint(0, 2)], 5)
                    enemy_resourc.add(enemy_mid)
                if e.type == ENEMY_BIG_PLANE:
                    enemy_big = EnemyPlane(list_big_enemy[random.randint(0, 1)], 3)
                    enemy_resourc.add(enemy_big)


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

    def __init__(self, image, speed=20):
        super().__init__(image, speed)
        self.hp = 5
        self.atk = 10
        self.rect.x = (SCREEN_WIDTH - hero_x) // 2
        self.rect.y = 3 * SCREEN_HEIGHT // 4
        self.bullets = pygame.sprite.Group()
        self.num = 1

    def move(self):
        # 获得键盘的操作事件
        e_key = pygame.key.get_pressed()
        # 对要按下按键类型进行判断
        if e_key[pygame.K_UP] or e_key[pygame.K_w]:
            print("向上运动")
            self.rect.y -= self.speed
        if e_key[pygame.K_DOWN] or e_key[pygame.K_s]:
            print("向下运动")
            self.rect.y += self.speed
        if e_key[pygame.K_LEFT] or e_key[pygame.K_a]:
            print("向左运动")
            self.rect.x -= self.speed
        if e_key[pygame.K_RIGHT] or e_key[pygame.K_d]:
            print("向右运动")
            self.rect.x += self.speed
        self.rect.x = 0 if self.rect.x < 0 else self.rect.x
        self.rect.x = SCREEN_WIDTH - 113 if self.rect.x > SCREEN_WIDTH - 113 else self.rect.x
        self.rect.y = 0 if self.rect.y < 0 else self.rect.y
        self.rect.y = SCREEN_HEIGHT - 105 if self.rect.y > SCREEN_HEIGHT - 105 else self.rect.y

        if e_key[pygame.K_k] or e_key[pygame.K_0]:
            self.num += 1
            if self.num == 20:
                self.fire()
                self.num = 0
        if e_key[pygame.K_f] or e_key[pygame.K_1]:
            self.num += 1
            if self.num == 20:
                self.fire2()
                self.num = 0

    def fire(self):
        # # 获得键盘的操作事件
        # e_key = pygame.key.get_pressed()
        # # 对要按下按键类型进行判断
        #
        # if e_key[pygame.K_k] or e_key[pygame.K_0]:
        print("开火")
        # 1.创建子弹精灵
        bullet = PlayerBullet(image="images/bullet/bullet_1.png", speed=8)
        bullet1 = PlayerBullet(image="images/bullet/bullet_1.png", speed=8)
        bullet2 = PlayerBullet(image="images/bullet/bullet_1.png", speed=8)
        bullet3 = PlayerBullet(image="images/bullet/bullet_1.png", speed=8)
        # 2.设置精灵的位置
        bullet.rect.centerx = self.rect.centerx + 15
        bullet.rect.bottom = self.rect.y + self.rect.height // 2
        bullet1.rect.centerx = self.rect.centerx - 15
        bullet1.rect.bottom = self.rect.y + self.rect.height // 2
        bullet2.rect.centerx = self.rect.centerx - 40
        bullet2.rect.bottom = self.rect.y + self.rect.height // 2 + 20
        bullet3.rect.centerx = self.rect.centerx + 40
        bullet3.rect.bottom = self.rect.y + self.rect.height // 2 + 20
        # 3.将精灵添加到精灵组
        self.bullets.add(bullet, bullet1, bullet2, bullet3)

    def fire2(self):
        bullet = PlayerBullet(image="images/bullet/bullet_default.png", speed=8)
        bullet.rect.centerx = self.rect.centerx - 40
        bullet.rect.bottom = self.rect.y + self.rect.height // 2
        bullet1 = PlayerBullet(image="images/bullet/bullet_default.png", speed=8)
        bullet1.rect.centerx = self.rect.centerx + 40
        bullet1.rect.bottom = self.rect.y + self.rect.height // 2

        self.bullets.add(bullet, bullet1)
    def be_ko(self):
        if self.hp <= 0:
            for i in range(1,5):
                bomb_image = Bomb("images/bomb/heroDeath"+ str(i) + ".png", 0, hero_image.rect.x, hero_image.rect.y)
                bomb = pygame.sprite.Group(bomb_image)
                bomb.draw(screen)
                bomb_image.kill()
                # pygame.time.wait(500)
                # bomb.update()
            # bomb_image.kill()
            # hero_image.kill()
            print("游戏结束")
            self.kill()
            return False
            # break
        else:
            return True


class EnemyPlane(GameSprite):
    """
    敌机飞机类
    """

    def __init__(self, image, speed=5):
        super().__init__(image, speed)
        self.direction = 'right'  # 定义敌机默认往右移动
        self.enemy_bullets = pygame.sprite.Group()
        self.rect.x = random.randint(0, (SCREEN_WIDTH - self.rect.width))
        self.rect.y = -self.rect.height
        self.hp = 1
        print(self.rect.x, self.rect.y)

    # def update(self):
    #     pass
    # # 让敌机沿垂直方向飞行
    # self.rect.y += self.speed
    # # 判断敌机是否飞出屏幕
    # if self.rect.y > SCREEN_HEIGHT:
    #     self.kill()

    def move(self):  # 左右摇摆
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.direction = 'left'
        elif self.rect.x < 0:
            self.direction = 'right'
        # def move(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

    def fire(self):
        # 发射子弹
        random_num = random.randint(1, 30)
        if random_num == 10 or random_num == 15:
            # 1.创建子弹精灵
            bullet = PlayerBullet(image="images/bullet/b2.png", speed=-8)
            # 2.设置精灵的位置
            bullet.rect.x = self.rect.x + self.rect.centerx // 2
            bullet.rect.y = self.rect.y + self.rect.height // 2
            # 3.将精灵添加到精灵组1
            self.enemy_bullets.add(bullet)
    def be_ko(self):
        if self.hp <= 0:
            for i in range(1,5):
                bomb_image = Bomb("images/bomb/heroDeath"+ str(i) + ".png", 0, hero_image.rect.x, hero_image.rect.y)
                bomb = pygame.sprite.Group(bomb_image)
                bomb.draw(screen)
            # bomb.update()
            # bomb_image.kill()
            # hero_image.kill()
            print("游戏结束")
            return False
            # break
        else:
            return True

    def update(self):
        self.move()
        self.fire()


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


class Bomb(GameSprite):

    def __init__(self, image, speed,x,y):
        super().__init__(image, speed)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.kill()
    def move(self):
        self.kill()


# 敌机图像资源
list_small_enemy = ["images/enemy/plane_s1.png",
                    "images/enemy/plane_s2.png",
                    "images/enemy/plane_s3.png",
                    "images/enemy/plane_s4.png",
                    "images/enemy/plane_s5.png"]

list_middle_enemy = ["images/enemy/plane_m1.png",
                     "images/enemy/plane_m2.png",
                     "images/enemy/plane_m3.png"]

list_big_enemy = ["images/enemy/boss1.png",
                  "images/enemy/boss2.png", ]
background_image1 = BackGround("images/bg/bg5.jpg")
background_image2 = BackGround("images/bg/bg5.jpg")
hero_image = PlayerPlane("images/hero/hero1.png")

# 设置背景图2的y值
background_image2.rect.y = -SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
# 创建一个精灵组
resource = pygame.sprite.Group(background_image1, background_image2, hero_image)
# 创建敌机精灵组
# enemy_resourc = pygame.sprite.Group(enemy_image, enemy_image1, enemy_image2)
enemy_resourc = pygame.sprite.Group()

# 控制每秒播放帧数
clock = pygame.time.Clock()

# 敌机产生事件
ENEMY_SMALL_PLANE = pygame.USEREVENT
ENEMY_MIDDLE_PLANE = pygame.USEREVENT + 1
ENEMY_BIG_PLANE = pygame.USEREVENT + 2
# pygame.time.set_timer(事件名，时间)定时器
pygame.time.set_timer(ENEMY_SMALL_PLANE, 1000)
pygame.time.set_timer(ENEMY_MIDDLE_PLANE, 5000)
pygame.time.set_timer(ENEMY_BIG_PLANE, 10000)


def play():

    while True:
        clock.tick(24)
        # 精灵组调用每个精灵的update方法
        resource.update()
        # 精灵组将所有精灵渲染到游戏窗口中
        resource.draw(screen)
        hero_image.update()

        hero_image.bullets.update()
        hero_image.bullets.draw(screen)

        enemy_resourc.draw(screen)
        enemy_resourc.update()

        # 碰撞检测
        # 精灵组与精灵组之间的碰撞
        pygame.sprite.groupcollide(hero_image.bullets, enemy_resourc, True, True)

        # 精灵与精灵组之间的碰撞
        if pygame.sprite.spritecollide(hero_image, enemy_resourc, True):
            hero_image.hp -= 1

        if hero_image.hp <= 0:

            hero_image.be_ko()
            print("游戏结束")
        if not hero_image.be_ko():
            break

        pygame.display.update()
play()
"""
# author Liu shi hao
# date: 2019/11/29 17:56
# file_name: plan
# 回顾之前的飞机大战
"""

import pygame
from pygame.locals import *
import time
import random

# 全局变量 表示爆炸
bomb_flag = 0  # 0 表示没有爆炸，1表示爆炸


# 敌机和英雄飞机的父类
class Plane(object):
    def __init__(self, screen, image_path, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        # 子弹列表
        self.bullet_list = []

    def display(self):
        # 显示英雄和敌机飞机
        self.screen.blit(self.image, (self.x, self.y))
        # 装越界的子弹
        bullet_list_remove = []
        # 显示子弹
        for bullet in self.bullet_list:
            # 显示和移动子弹
            bullet.display()
            bullet.move()
            # 判断子弹是否越界
            if bullet.judge():
                bullet_list_remove.append(bullet)
        # 删除越界的子弹
        for i in bullet_list_remove:
            self.bullet_list.remove(i)


class HeroPlane(Plane):
    def __init__(self, screen):
        image_path = 'images/hero/hero1.png'
        super(HeroPlane, self).__init__(screen, image_path, 190, 500)
        # 添加爆炸效果
        self.bomb_image_list = []
        self.__get_bomb_image()  # 加载爆炸图片
        self.isbomb = False  # false没有爆炸，True爆炸
        self.image_num = 0  # 显示过的图片数
        self.image_index = 0  # 显示图片的下标变化

    def display(self):
        if self.isbomb:
            bomb_image = self.bomb_image_list[self.image_index]
            self.screen.blit(bomb_image, (self.x, self.y))
            self.image_num += 1
            if self.image_num == (self.image_length + 1):
                self.image_num = 0
                self.image_index += 1

                if self.image_index > (self.image_length - 1):
                    self.image_index = 5
                    time.sleep(2)
                    exit()
        else:
            # 调用父类方法正常显示飞机
            Plane.display(self)
            # 遍历子弹是否击中飞机
            for bullet in self.bullet_list:
                # 判断当前子弹是否击中飞机
                if bullet.judge_jizhong(self.enemy):
                    self.enemy.bomb(True)

    def bomb(self, isbomb):
        self.isbomb = isbomb

    # 加载爆炸图片
    def __get_bomb_image(self):
        for i in range(1, 4):
            im_path = 'images/bomb/heroDeath' + str(i) + '.png'
            self.bomb_image_list.append(pygame.image.load(im_path))
        # 总数有多少张
        self.image_length = len(self.bomb_image_list)

    # 发射子弹

    def send_bullet(self, enemy):
        self.enemy = enemy
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

    # 左移动
    def move_left(self):
        self.x -= 5

    # 右移动
    def move_right(self):
        self.x += 5

    # 向上移动
    def move_up(self):
        self.y -= 5

    # 向下移动
    def move_down(self):
        self.y += 5


class EnemyPlane(Plane):
    def __init__(self, screen):
        image_path = 'images/enemy/plane_s2.png'
        self.direction = 'right'
        super(EnemyPlane, self).__init__(screen, image_path, 10, 10)

        # 添加爆炸效果
        self.bomb_image_list = []
        self.__get_bomb_image()  # 加载爆炸图片
        self.isbomb = False  # false没有爆炸，True爆炸
        self.image_num = 0  # 显示过的图片数
        self.image_index = 0  # 显示图片的下标变化

    def bomb(self, isbomb):
        self.isbomb = isbomb

    # 加载爆炸图片
    def __get_bomb_image(self):
        for i in range(1, 4):
            im_path = 'images/bomb/heroDeath' + str(i) + '.png'
            self.bomb_image_list.append(pygame.image.load(im_path))
        # 总数有多少张
        self.image_length = len(self.bomb_image_list)

    def display(self):
        # 判断是否要爆炸
        if self.isbomb:
            bomb_image = self.bomb_image_list[self.image_index]
            self.screen.blit(bomb_image, (self.x, self.y))
            self.image_num += 1
            if self.image_num == (self.image_length + 1):
                self.image_num = 0
                self.image_index += 1

                if self.image_index > (self.image_length - 1):
                    self.image_index = 5
                    time.sleep(2)
                    exit()
        else:
            Plane.display(self)
            for bullet in self.bullet_list:
                # 判断当前子弹是否击中飞机
                if bullet.judge_jizhong(self.hero):
                    self.hero.bomb(True)

    # 敌机发射子弹
    def send_bullet(self, hero):
        self.hero = hero
        random_num = random.randint(1, 100)
        if random_num == 10 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

    def move(self):
        if self.direction == 'right':
            self.x += 2
        elif self.direction == 'left':
            self.x -= 2
        # 判断有没有越界
        if self.x > 480 - 51:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'


# 子弹父类
class BaseBullet(object):
    def __init__(self, screen, image_path, x, y):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y

    # 显示飞机
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


# 敌机的子弹类
class EnemyBullet(BaseBullet):
    def __init__(self, screen, x, y):
        image_path = 'images/bullet/b2.png'
        super(EnemyBullet, self).__init__(screen, image_path, x + 20, y + 30)

    def judge_jizhong(self, hero):
        if self.x > hero.x and self.x < hero.x + 50:
            if self.y > hero.y and self.y < hero.y + 20:
                print('英雄死亡')
                return True
        else:
            return False

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 700:
            return True
        else:
            return False


# 英雄的子弹类
class Bullet(BaseBullet):
    def __init__(self, screen, x, y):
        image_path = 'images/bullet/bullet_1.png'
        super(Bullet, self).__init__(screen, image_path, x + 40, y - 20)

    def judge_jizhong(self, enemy):
        if self.x > enemy.x and self.x < enemy.x + 56:
            if self.y > enemy.y and self.y < enemy.y + 31:
                print('击中敌机')
                return True
        else:
            return False

    def move(self):
        self.y -= 5

    # 判断子弹是否越界
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class PlaneGame(object):
    # 键盘控制
    def key_control(self):
        # 监听键盘的代码
        for event in pygame.event.get():
            # 是否点击退按钮
            if event.type == QUIT:
                print('exit')
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    print('left')
                    self.hero.x -= 5
                elif event.key == K_RIGHT or event.key == K_d:
                    print('right')
                    self.hero.x += 5
                elif event.key == K_UP or event.key == K_w:
                    # 上方向键
                    print("up")
                    self.hero.y -= 5
                elif event.key == K_DOWN or event.key == K_s:
                    # 下方向键
                    print("down")
                    self.hero.y += 5
                elif event.key == K_SPACE:
                    # 上方向键
                    print("space-空格建")
                    self.hero.send_bullet(self.enemy)
                elif event.key == K_b:
                    # 按b键了
                    print("爆炸")
                    self.enemy.isbomb = True

    def main(self):
        pygame.init()
        # 设置键盘重复键
        pygame.key.set_repeat()
        # 创建一个窗口，用来显示内容
        self.screen = pygame.display.set_mode((480, 700), 0, 32)
        # 创建一个和窗口大小的图片，用来充当背景
        self.background = pygame.image.load("images/bg/bg1.jpg")
        # 初始化英雄飞机对象
        self.hero = HeroPlane(self.screen)
        # 初始化敌机实例对象
        self.enemy = EnemyPlane(self.screen)

        while True:
            # 键盘控制
            self.key_control()
            # 把背景图片贴到窗口上
            self.screen.blit(self.background, (0, 0))
            # 把英雄飞机贴到窗口上显示
            # screen.blit(hero,(x,y))
            self.hero.display()
            # 显示敌机
            self.enemy.display()
            self.enemy.move()
            self.enemy.send_bullet(self.hero)
            # 更新窗口重新绘制
            pygame.display.update()
            # 让cpu休息一会会
            time.sleep(0.01)


if __name__ == "__main__":
    PlaneGame().main()

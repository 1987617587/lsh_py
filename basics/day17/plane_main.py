"""
# author Liu shi hao
# date: 2019/11/29 18:40
# file_name: plane_main

"""
import pygame
import random
from plane_sprite import *

# 定义定时常量
CREATE_ENEMY = pygame.USEREVENT

# 定义英雄开火定时常量
FIRE = pygame.USEREVENT + 1


class Plane_game(object):

    # 初始化
    def __init__(self):

        # 显示主界面
        self.screen = pygame.display.set_mode((480, 852))
        self.__create_sprites__()
        pygame.time.set_timer(CREATE_ENEMY, 1000)
        pygame.time.set_timer(FIRE, 300)
        self.clock = pygame.time.Clock()
        self.clock1 = pygame.time.Clock()

    # 开始游戏
    def start_game(self):

        while True:

            # 设置英雄毁灭时的帧率
            if self.hero.name == 3:
                self.time = 3
            else:
                self.time = 60

            self.clock.tick(self.time)
            self.__check_collide()
            self.__event_handler()
            self.__update()

            # 显示图像
            pygame.display.update()

    # 更新显示
    def __update(self):

        # 显示背景
        self.back_group.update()
        self.back_group.draw(self.screen)

        # 显示敌人
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 显示英雄
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 显示子弹
        self.bullet_group.update()
        self.bullet_group.draw(self.screen)

    # 创建精灵类
    def __create_sprites__(self):

        # 创建背景精灵类
        self.back = bg()
        self.back1 = bg()
        self.back1.rect.y = -852
        self.back_group = pygame.sprite.Group(self.back, self.back1)

        # 创建敌人精灵类
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建子弹类
        self.bullet_group = pygame.sprite.Group()

        # 创建敌机碰撞精灵组
        self.enemy_hit_group = pygame.sprite.Group()

    # 检查碰撞
    def __check_collide(self):

        if self.hero.i == 5:
            self.hero.kill()
            self.__game_over__()

        # 子弹消灭敌机
        # 在敌机被消灭时显示爆炸过程
        # 敌机与子弹相撞时先不移除敌机精灵
        enemy_hit = pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, False, True)
        self.enemy_hit_group.add(enemy_hit)
        for enemy1 in self.enemy_hit_group:
            if enemy1.explode_index == 0:

                # 判断是否输出爆炸效果图
                enemy1.explode_index = 1

            # 判断在爆炸效果图输完后删除精灵
            elif enemy1.explode_index == 5:
                self.enemy_hit_group.remove_internal(enemy1)
                self.enemy_group.remove_internal(enemy1)

        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # 英雄爆炸
            self.hero.name = 3

    # 事件处理
    def __event_handler(self):

        for event in pygame.event.get():
            # 结束游戏
            if event.type == pygame.QUIT:
                self.__game_over__()

            # 定时创建敌人精灵
            elif event.type == CREATE_ENEMY:
                self.enemy = Enemy()
                self.enemy_group.add(self.enemy)

            # 定时发射子弹
            elif event.type == FIRE:
                for i in (0, 1, 2):
                    # self.clock1.tick(30)
                    self.bullet = Bullet()
                    self.bullet.rect.centerx = self.hero.rect.centerx
                    self.bullet.rect.y = self.hero.rect.y - i * 6 * 1.5
                    self.bullet_group.add(self.bullet)

        # 左右移动英雄
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 4
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -4

    # 游戏结束
    def __game_over__(self):
        print("游戏结束")
        pygame.quit()
        exit()


# BG精灵类
class bg(GameSprite):

    def __init__(self):
        super().__init__("./images/background.png")

    def update(self):
        # 背景滚动
        super().update()
        if self.rect.y >= 852:
            self.rect.y = (-self.rect.height)


# 敌机类
class Enemy(GameSprite):

    def __init__(self):
        print("敌机出厂")
        super().__init__("./images/enemy0.png")
        self.speed = random.randint(2, 6)
        self.rect.x = random.randint(0, 480 - self.rect.width)
        self.rect.y = -self.rect.height
        self.explode_index = 0

    def update(self):
        super().update()

        # 删除敌机
        if self.rect.y >= 852:
            print("请销毁敌机")
            self.kill()
        # 销毁敌机
        if self.explode_index == 5:
            # self.kill()
            return

        # 敌机爆炸
        if self.explode_index != 0:
            new_rect = self.rect
            super().__init__("./images/enemy0_down%d.png" % self.explode_index)
            self.explode_index += 1
            self.rect = new_rect

    def __del__(self):
        print("销毁敌机")


# 英雄类
class Hero(GameSprite):

    def __init__(self):
        super().__init__("./images/hero1.png")
        self.rect.bottom = 730
        self.rect.x = 240 - self.rect.width / 2
        self.speed = 0
        self.name = 1
        self.clock = pygame.time.Clock()
        self.i = 1

    def update(self):

        self.rect.x += self.speed
        new_rect = self.rect
        if self.name == 1:
            super().__init__("./images/hero%d.png" % 2)
            self.speed = 0
            self.name = 2
        elif self.name == 2:
            super().__init__("./images/hero%d.png" % (1))
            self.speed = 0
            self.name = 1

        # 英雄毁灭
        elif self.name == 3:
            super().__init__("./images/hero_blowup_n%d.png" % self.i)
            self.rect.centerx = new_rect.centerx
            self.rect.centery = new_rect.centery
            self.i += 1
            return
        self.rect = new_rect
        # 防止英雄出界
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 480 - self.rect.width:
            self.rect.x = 480 - self.rect.width

    def explode(self, screen):

        new_rect = self.rect
        for i in (1, 2, 3, 4):
            self.clock.tick(1)
            super().__init__("./images/hero_blowup_n%d.png" % i)
            self.rect.centerx = new_rect.centerx
            self.rect.centery = new_rect.centery
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pygame.display.update()


# 子弹类
class Bullet(GameSprite):

    def __init__(self):
        super().__init__("./images/bullet1.png", -5)

    def update(self):
        super().update()

        if self.rect.y <= 0:
            self.kill()


# 主函数调用
play_game = Plane_game()
play_game.start_game()

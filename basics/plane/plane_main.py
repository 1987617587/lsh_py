# author : liuShiHao
# Date : 2019/8/11 20:31
import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 512, 768)

# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵的创建(image/rect/speed)
        image_name = "images2/bg/bg4.jpg"
        super().__init__(image_name)

        # 2.判断是否交替图像，如果是需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出屏幕，将设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("images2/enemy/plane_m2.png")
        # 2.设置敌机的随机初始速度
        self.speed = random.randint(1, 3)

        # 3.设置敌机的随机初始位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类方法，让敌机在垂直方向上运动
        super().update()

        # 2.调用是否飞出屏幕，如果是，需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕...")

            # kill方法将精灵从所有精灵组中移出
            self.kill()

    def __del__(self):
        pass
        # print("敌机挂了 %s" % self.rect)


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1.调用父类方法，设置image/speed
        super().__init__("images2/hero/hero4.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向上移动
        self.rect.x += self.speed
        self.rect.y += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")
        for i in (1, 2, 3):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置精灵的位置
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i * 20
            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)

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
        self.rect.x = SCREEN_RECT.x - 131 if self.rect.x > SCREEN_RECT.x - 131 else self.rect.x
        self.rect.y = 0 if self.rect.y < 0 else self.rect.y
        self.rect.y = SCREEN_RECT.y - 105 if self.rect.y > SCREEN_RECT.y - 105 else self.rect.y


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("images2/bullet/bullet_2.png", -2)

    def update(self):
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
        # print("子弹被销毁...")

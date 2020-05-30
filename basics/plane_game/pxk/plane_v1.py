"""
API:
application program interface
programer

OOP
OOD
OOT
OOA
"""
import pygame,random

pygame.init()
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768

class GameSprite(pygame.sprite.Sprite):
    """游戏超级父类"""

    def __init__(self,image,speed):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def move(self):
        pass

    def event(self):
        e_list = pygame.event.get()
        if len(e_list) > 0:
            for e in e_list:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if e.type == ENEMY_SMALL_EVENT:
                    #创建小敌机
                    enemy_small = EnemySprite("images/enemy/plane_s1.png",8)
                    enemy_resource.add(enemy_small)
                if e.type == ENEMY_MIDDLE_EVENT:
                    enemy_middle = EnemySprite("images/enemy/plane_m1.png",5)
                    enemy_resource.add(enemy_middle)
                if e.type == ENEMY_BIG_EVENT:
                    enemy_big = EnemySprite("images/enemy/boss1.png",3)
                    enemy_resource.add(enemy_big)

    def update(self):
        self.event()
        self.move()

class BackgroundImageSprite(GameSprite):
    """背景精灵类"""
    def move(self):
        #控制边界判断
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = - SCREEN_HEIGHT

class HeroSprite(GameSprite):
    """英雄飞机精灵类"""
    def __init__(self, image, speed):
        super().__init__(image, speed)
        self.rect.x = (SCREEN_WIDTH - 114)//2
        self.rect.y = SCREEN_HEIGHT*2//3
        self.bullets_group = pygame.sprite.Group()
        #控制子弹产生数量
        self.bullet_num = 0

    def move(self):
        #边界判断
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - 114:
            self.rect.x = SCREEN_WIDTH -114
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > SCREEN_HEIGHT - 93:
            self.rect.y = SCREEN_HEIGHT -93


    def event(self):
        #事件操作方法
        # 获得键盘事件
        e_key = pygame.key.get_pressed()
        if e_key[pygame.K_UP]:
            self.rect.y -= self.speed
        if e_key[pygame.K_DOWN]:
            self.rect.y += self.speed
        if e_key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if e_key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if e_key[pygame.K_SPACE]:
            print("开火")
            self.fire()

    def fire(self):
        #开火方法
        print("开火")
        self.bullet_num += 1
        if self.bullet_num % 6 ==0:
            self.bullet_num = 0
            bullet = BulletSprite("images/bullet/bullet_1.png",8,self.rect.centerx-22,self.rect.centery-68)
            # bullet1 = BulletSprite("images/bullet/bullet_1.png",8,self.rect.centerx-80,self.rect.centery-50)
            # bullet2 = BulletSprite("images/bullet/bullet_1.png",8,self.rect.centerx+30,self.rect.centery-50)
            # self.bullets_group.add(bullet,bullet1,bullet2)
            self.bullets_group.add(bullet)
class BulletSprite(GameSprite):
    """子弹精灵类"""
    def __init__(self, image, speed,x,y):
        super().__init__(image, speed)
        self.rect.x = x
        self.rect.y = y

    def move(self):
        #边界判断
        self.rect.y -= self.speed
        if self.rect.y < - self.rect.height:
            self.kill()

class EnemySprite(GameSprite):

    def __init__(self, image, speed):
        super().__init__(image, speed)
        self.rect.x = random.randint(0,(SCREEN_WIDTH-self.rect.width))
        self.rect.y = -self.rect.height

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

#自定义敌方飞机的自定义事件
#USEREVENT
ENEMY_SMALL_EVENT = pygame.USEREVENT #24
ENEMY_MIDDLE_EVENT = pygame.USEREVENT + 1 #25
ENEMY_BIG_EVENT = pygame.USEREVENT + 2

#pygame.time.set_timer(事件名，时间)定时器
pygame.time.set_timer(ENEMY_SMALL_EVENT,1000)
pygame.time.set_timer(ENEMY_MIDDLE_EVENT,3000)
pygame.time.set_timer(ENEMY_BIG_EVENT,5000)

#创建的实例对象
background_image1 = BackgroundImageSprite("images/bg/bg5.jpg",5)
background_image2 = BackgroundImageSprite("images/bg/bg5.jpg",5)
#初始化背景图片2的高度
background_image2.rect.y = -SCREEN_HEIGHT
hero = HeroSprite("images/hero/hero4.png",5)

#搭建窗口
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,24)

#游戏精灵组
resource = pygame.sprite.Group(background_image1,background_image2,hero)
#敌方飞机精灵组
enemy_resource = pygame.sprite.Group()

#时钟对象控制每秒播放的频率
clock = pygame.time.Clock()

while True:
    clock.tick(24)
    #精灵组自动调用每个精灵的update方法
    resource.update()
    resource.draw(screen)

    enemy_resource.update()
    enemy_resource.draw(screen)

    hero.bullets_group.update()
    hero.bullets_group.draw(screen)

    #碰撞检测
    #精灵组与精灵组之间的碰撞
    pygame.sprite.groupcollide(hero.bullets_group,enemy_resource,True,True)
    #精灵与精灵组之间的碰撞
    pygame.sprite.spritecollide(hero,enemy_resource,True)
    pygame.display.update()





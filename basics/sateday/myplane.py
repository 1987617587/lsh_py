"""
# author Liu shi hao
# date: 2019/11/30 9:32
# file_name: myplane

"""
import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/hero/hero1.png")
        self.image2 = pygame.image.load("images/hero/hero1.2.png")
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images\\bomb\\heroDeath1.png").convert_alpha(),
            pygame.image.load("images\\bomb\\heroDeath2.png").convert_alpha(),
            pygame.image.load("images\\bomb\\heroDeath3.png").convert_alpha(),
            pygame.image.load("images\\bomb\\heroDeath4.png").convert_alpha(),
            pygame.image.load("images\\bomb\\heroDeath5.png").convert_alpha(),
            pygame.image.load("images\\bomb\\heroDeath6.png").convert_alpha()
        ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, self.height - self.rect.height - 60
        self.speed = 10
        self.active = True

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
        self.rect.x = self.width - 113 if self.rect.x > self.width - 113 else self.rect.x
        self.rect.y = 0 if self.rect.y < 0 else self.rect.y
        self.rect.y = self.height - 105 if self.rect.y > self.height - 105 else self.rect.y

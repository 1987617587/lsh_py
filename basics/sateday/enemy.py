"""
# author Liu shi hao
# date: 2019/11/30 10:11
# file_name: enemy

"""
from random import randint

import pygame


class SmallEnemy(pygame.sprite.Sprite):
    mp = 1
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        for i in range(1, 6):
            self.images = pygame.image.load("images/enemy/plane_s" + str(i) + ".png").convert_alpha()
        self.rect = self.images.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 3
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images\\bomb\heroDeath1.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath2.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath3.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath4.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath5.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath6.png").convert_alpha()
        ])
        self.mp = SmallEnemy.mp

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.mp = SmallEnemy.mp
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)


class MidEnemy(pygame.sprite.Sprite):
    mp = 10

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        for i in range(1, 4):
            self.images = pygame.image.load("images/enemy/plane_m" + str(i) + ".png").convert_alpha()
        self.rect = self.images.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height,
                                                                                          -self.height)
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images\\bomb\heroDeath1.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath2.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath3.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath4.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath5.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath6.png").convert_alpha()
        ])
        self.mp = MidEnemy.mp

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.mp = MidEnemy.mp
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height,
                                                                                          -self.height)


class BigEnemy(pygame.sprite.Sprite):
    mp = 25

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        for i in range(1, 3):
            self.images = pygame.image.load("images/enemy/boss" + str(i) + ".png").convert_alpha()
        self.rect = self.images.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15 * self.height,
                                                                                          -5 * self.height)
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("images\\bomb\heroDeath1.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath2.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath3.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath4.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath5.png").convert_alpha(),
            pygame.image.load("images\\bomb\heroDeath6.png").convert_alpha()
        ])
        self.mp = BigEnemy.mp

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.mp = BigEnemy.mp
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15 * self.height,
                                                                                          -5 * self.height)

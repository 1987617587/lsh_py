"""
# author Liu shi hao
# date: 2019/11/29 18:40
# file_name: plane_sprite

"""
import pygame

class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1):

        super().__init__()

        self.image=pygame.image.load(image_name)

        self.rect=self.image.get_rect()

        self.speed=speed

    def update(self):

        self.rect.y+=self.speed



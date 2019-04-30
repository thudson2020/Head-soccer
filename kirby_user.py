import pygame, sys, time, random
from pygame.locals import *
KIRBY=pygame.image.load('kirby_normal.png')
class kirby_user(pygame.sprite.Sprite):
    def __init__(self, ground):
        super().__init__()
        self.health=500
        self.x=50
        self.y=ground
        self.image=KIRBY
        self.rect=pygame.Rect(self.x,self.y,75,75)
    def left(self):
        self.rect.x=self.rect.x-5
    def right(self):
        self.rect.x=self.rect.x+5
    def jump(self,y):
        self.y=self.rect.y=250+(((y-7)**2)-49)

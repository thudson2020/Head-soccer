import pygame, sys, time, random
from pygame.locals import *
KIRBY=pygame.image.load('kirby_normal.png')
class user(pygame.sprite.Sprite):
    def __init__(self, ground):
        super().__init__()
        self.x=50
        self.y=ground-44
        self.image=KIRBY
        self.rect=pygame.Rect(self.x,self.y,50,50)
    def left(self):
        self.rect.x=self.rect.x-5
    def right(self):
        self.rect.x=self.rect.x+5
    def jump(self,y):
        self.y=self.rect.y=306+(((y-9)**2)-81)

import pygame, sys, time, random
from pygame.locals import *
SHOE=pygame.image.load('shoe.png')
class user(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.image=SHOE
        self.rect=pygame.Rect(self.x,self.y,18,10)

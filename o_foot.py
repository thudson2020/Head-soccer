import pygame, sys, time, random, math
from pygame.locals import *
SHOE=pygame.image.load('shoe.png')
class o__foot(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.x=x
        self.y=y+25
        self.image=SHOE
        self.rotation=0
        self.rect=pygame.Rect(self.x,self.y,18,10)
    def attatch(self,x,y):
        self.rect.x=x
        self.rect.y=y+25
    def rotation_out(self,x,y):
        self.rect.x=x-25
        self.rect.y=y+25

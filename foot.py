import pygame, sys, time, random, math
from pygame.locals import *
SHOE=pygame.image.load('shoe.png')
class foot(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.x=x
        self.y=y-50
        self.image=SHOE
        self.rotation=0
        self.rect=pygame.Rect(self.x,self.y,18,10)
    def attatch(self,x,y,xx,yy):
        self.rect.x=x+xx+25
        self.rect.y=y+yy+25
    def rotation_out(self,x,y):
        y=y+5
        x=x+5
    def roatation_back(self,x,y):
        x=x-5
        y=y-5
    def attatch_two():
        self.rect.x=x+xx-25
        self.rect.y=y+yy+25

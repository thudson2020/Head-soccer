import pygame, sys, time, random
from pygame.locals import *
BALL= pygame.image.load('ball.png')
class ball (pygame.sprite.Sprite):
    def __init__(self,ground):
        super().__init__()
        self.x=475
        self.y=ground-250
        self.y_v=0
        self.x_v=0
        self.image=BALL
        self.rect=pygame.Rect(self.x,self.y, 50,50)

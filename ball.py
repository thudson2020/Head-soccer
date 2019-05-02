import pygame, sys, time, random
from pygame.locals import *
BALL= pygame.image.load('ball.png')
class ball (pygame.sprite.Sprite):
    def __init__(self,ground):
        super().__init__()
        self.x=475
        self.y=ground-249
        self.y_v=0
        self.x_v=0
        self.image=BALL
        self.rect=pygame.Rect(self.x,self.y, 49,49)
    def vert_move(self):
        self.y=self.y-self.y_v
    def gravity(self,g_m):
        self.y_v=self.y_v+(-5)

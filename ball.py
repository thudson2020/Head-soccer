import pygame, sys, time, random
from pygame.locals import *
BALL= pygame.image.load('ball.png')
class ball (pygame.sprite.Sprite):
    def __init__(self,ground):
        super().__init__()
        self.x=475
        self.y=ground-150
        self.y_v=0
        self.x_v=0
        self.image=BALL
        self.rect=pygame.Rect(self.x,self.y, 50,50)
    #so the ball has more fluid movements and doesn't snap between velocities
    def horz_move(self,v):
        self.rect.x=self.rect.x+v
    def vert_move(self,v):
        self.rect.y=self.rect.y+v

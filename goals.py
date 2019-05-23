import pygame, sys, time, random
from pygame.locals import *
GOAL=[pygame.image.load('goal_left.png'),pygame.image.load('goal_right.png')]
class goals(pygame.sprite.Sprite):
    def __init__(self, ground,side,x):
        super().__init__()
        self.x=side
        self.y=ground-100
        self.image=GOAL[x]
        self.rect=pygame.Rect(self.x,self.y,50,100)
#goal sprite so it can have a hitbox and allow easier interaction with the ball

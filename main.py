import pygame, sys, time, random
from pygame.locals import *
from user import user
from goals import goals
DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("ball")
ground=350
BLACK=(0,0,0)
WHITE=(255,255,255)
FPS=30
fpsClock = pygame.time.Clock()
user=user(ground)
user_goal=goals(ground,0,0)
o_goal=goals(ground,950,1)
def update(x):
    DISPLAYSURF.blit(x.image,x.rect)
move_up=False
move_down=False
move_left=False
move_right=False
jump_time=0
while True:
    DISPLAYSURF.fill(BLACK)
    pygame.draw.line(DISPLAYSURF, WHITE, (0, 350), (1000, 350), 4)
    for event in pygame.event.get():
        if event.type== KEYDOWN:
            if(event.key==K_UP):
                move_up=True
            if event.key == K_LEFT:
                move_left=True
            if event.key == K_RIGHT:
                move_right=True
        if event.type==KEYUP:
            if event.key == K_UP:
                move_up=False
            if event.key == K_LEFT:
                move_left=False
            if event.key == K_RIGHT:
                move_right=False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if move_left==True:
        user.left()
    if move_right==True:
        user.right()
    if move_up==True:
        user.jump(jump_time)
        jump_time=jump_time+1
        if jump_time>14:
            jump_time=1
    if move_up==False:
        if jump_time!=0:
            user.jump(jump_time)
            jump_time=jump_time+1
        if jump_time>14:
            jump_time=0
    update(user)
    update(user_goal)
    update(o_goal)
    pygame.display.update()
    fpsClock.tick(FPS)

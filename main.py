import pygame, sys, time, random
from pygame.locals import *
from user import user
from goals import goals
from ball import ball
DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("ball")
ground=350
BLACK=(0,0,0)
WHITE=(255,255,255)
gravity=-10
y_v=-4
g_m=0
FPS=60
x_v=5
fpsClock = pygame.time.Clock()
user=user(ground)
user_goal=goals(ground,0,0)
o_goal=goals(ground,950,1)
game_ball=ball(ground)
def update(x):
    DISPLAYSURF.blit(x.image,x.rect)
def vert_move():
    global g_m, game_ball
    game_ball.rect.y=game_ball.rect.y+4
    g_m=g_m+1
bounce='False'
ball_move_r=False
ball_move_l=False
def collision(x,y):
    global ball_move_l,ball_move_r
    if pygame.sprite.collide_rect(x,y):
        if user.rect.x+25<=game_ball.rect.x:
            ball_move_r=True
        else:
            ball_move_l=True
l=0
def x_move():
    global ball_move_l,ball_move_r,x_v,l
    if ball_move_r==True:
        ball_move_l=False
        if l%5==0:
            x_v=x_v-1
        l=l+1
    if ball_move_l==True:
        ball_move_r=False
        if l%5==0:
            x_v=x_v-1
        l=l+1
    if x_v==0:
        l=0
        ball_move_r=False
        ball_move_l=False
        x_v=5
#def gravity(g_m):
    #global y_v
    #y_v=y_v+(-2)
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
        if jump_time>18:
            jump_time=1
    if move_up==False:
        if jump_time!=0:
            user.jump(jump_time)
            jump_time=jump_time+1
        if jump_time>18:
            jump_time=0
    '''
    #if game_ball.rect.y<ground-50:
        #gravity(g_m)
    if game_ball.rect.y<ground-50 and bounce=='False':
        vert_move()
    if game_ball.rect.y==ground-50:
        g_m=g_m-2
        bounce='True'
    if bounce=='True':
        game_ball.rect.y=game_ball.rect.y-4
        g_m=g_m-1
    if g_m==0:
        bounce='False'
    '''
    update(user)
    update(user_goal)
    update(o_goal)
    update(game_ball)
    collision(user,game_ball)
    x_move()
    if ball_move_r==True:
        game_ball.right(x_v)
    if ball_move_l==True:
        game_ball.left(x_v)

    pygame.display.update()
    fpsClock.tick(FPS)

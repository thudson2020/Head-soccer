import pygame, sys, time, random,math
from pygame.locals import *
from user import user
from goals import goals
from ball import ball
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("ball")
ground=350
BLACK=(0,0,0)
WHITE=(255,255,255)
g_m=0
FPS=60
x_v=10
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
jump_hit=False
ground_pinch=False
def collision(x,y):
    global ball_move_l,ball_move_r,jump_hit,y_v
    if pygame.sprite.collide_rect(x,y):
        if user.rect.x+25<=game_ball.rect.x:
            ball_move_r=True
        else:
            ball_move_l=True
        if user.rect.y+25>=game_ball.rect.y:
            jump_hit=True
        if user.rect.y-25>game_ball.rect.y:
            if game_ball.rect.y!=ground-50:
                y_v=y_v+2
            else:
                y_v=y_v+5

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
        x_v=10
def check_wall():
    global ball_move_l,ball_move_r
    if ball_move_r==True and game_ball.rect.x>=950:
        ball_move_r= False
        ball_move_l= True
    if ball_move_l==True and game_ball.rect.x<=0:
        ball_move_l=False
        ball_move_r=True
y_v=0
def ball_gravity():
    global y_v
    y_v=y_v+1
def total_y_move():
    global y_v,jump_hit
    if game_ball.rect.y+50>=ground and y_v>0:
        y_v=(-y_v)+2
    if jump_hit==True:
        y_v=-10
        jump_hit=False
    game_ball.vert_move(y_v)
    ball_gravity()
def display_message(text, x, y, s):
    BASICFONT= pygame.font.Font('freesansbold.ttf',s)
    Surf= BASICFONT.render(text,1,(WHITE))
    Rect =Surf.get_rect()
    Rect.topleft=(x,y)
    DISPLAYSURF.blit(Surf,Rect)
display_u_goal=False
display_o_goal=False
def goal():
    global display_u_goal,display_o_goal
    if game_ball.rect.x>=925 and game_ball.rect.y>=o_goal.rect.y:
        display_u_goal=True
    if game_ball.rect.x<=25 and game_ball.rect.y>=user_goal.rect.y:
        display_o_goal=True
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
    update(user)
    update(user_goal)
    update(o_goal)
    update(game_ball)
    collision(user,game_ball)
    x_move()
    check_wall()
    goal()
    total_y_move()
    if display_o_goal==True:
        display_message('opponent goal',420,250, 32)
    if display_u_goal==True:
        display_message('user goal',430,250,32)
    if ball_move_r==True:
        game_ball.right(x_v)
    if ball_move_l==True:
        game_ball.left(x_v)
    pygame.display.update()
    fpsClock.tick(FPS)

import pygame, sys, time, random,math
from pygame.locals import *
from user import user
from goals import goals
from ball import ball
from foot import foot
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("ball")
ground=350
BLACK=(0,0,0)
WHITE=(255,255,255)
FPS=60
x_v=0
fpsClock = pygame.time.Clock()
user=user(ground)
user_goal=goals(ground,0,0)
o_goal=goals(ground,950,1)
game_ball=ball(ground)
user_foot=foot(user.rect.x,user.rect.y)
def update(x):
    DISPLAYSURF.blit(x.image,x.rect)
y_v=0
collision=False
wait=0
def collision(x,y):
    global x_v, y_v, wait
    if pygame.sprite.collide_rect(x,y) and wait==0:
        # y angle
        if user.rect.x+25>game_ball.rect.x+5:
            x_v=-5
        elif user.rect.x+25<= game_ball.rect.x+5 and user.rect.x> game_ball.rect.x+10:
            x_v=-4
        elif user.rect.x+25<= game_ball.rect.x+10 and user.rect.x> game_ball.rect.x+15:
            x_v=-3
        elif user.rect.x+25<= game_ball.rect.x+15 and user.rect.x> game_ball.rect.x+20:
            x_v=-2
        elif user.rect.x+25<= game_ball.rect.x+20 and user.rect.x> game_ball.rect.x+23:
            x_v=-1
        elif user.rect.x+25<= game_ball.rect.x+23 and user.rect.x> game_ball.rect.x+27:
            x_v=0
        elif user.rect.x+25<= game_ball.rect.x+27 and user.rect.x> game_ball.rect.x+30:
            x_v=1
        elif user.rect.x+25<= game_ball.rect.x+30 and user.rect.x> game_ball.rect.x+35:
            x_v=2
        elif user.rect.x+25<= game_ball.rect.x+35 and user.rect.x> game_ball.rect.x+40:
            x_v=3
        elif user.rect.x+25<= game_ball.rect.x+40 and user.rect.x> game_ball.rect.x+45:
            x_v=4
        elif user.rect.x+25<= game_ball.rect.x+45:
            x_v=5
        # x angle
        if user.rect.y+22<game_ball.rect.y+5:
            y_v=y_v-5
        elif user.rect.y+22>=game_ball.rect.y+5 and user.rect.y<game_ball.rect.y+10:
            y_v=y_v-4
        elif user.rect.y+22>=game_ball.rect.y+10 and user.rect.y<game_ball.rect.y+15:
            y_v=y_v-3
        elif user.rect.y+22>=game_ball.rect.y+15 and user.rect.y<game_ball.rect.y+20:
            y_v=y_v-2
        elif user.rect.y+22>=game_ball.rect.y+20 and user.rect.y<game_ball.rect.y+23:
            y_v=y_v-1
        elif user.rect.y+22>=game_ball.rect.y+23 and user.rect.y<game_ball.rect.y+27:
            y_v=y_v+0
        elif user.rect.y+22>=game_ball.rect.y+27 and user.rect.y<game_ball.rect.y+30:
            y_v=y_v+1
        elif user.rect.y+22>=game_ball.rect.y+30 and user.rect.y<game_ball.rect.y+35:
            y_v=y_v+2
        elif user.rect.y+22>=game_ball.rect.y+35 and user.rect.y<game_ball.rect.y+40:
            y_v=y_v+3
        elif user.rect.y+22>=game_ball.rect.y+40 and user.rect.y<game_ball.rect.y+45:
            y_v=y_v+4
        elif user.rect.y+22>=game_ball.rect.y+45:
            y_v=y_v+5
        wait=3
def foot_collision(f,b):
    global y_v, x_v, wait
    if pygame.sprite.collide_rect(f,b) and wait==0:
        if f.rect.y>b.rect.y-20:
            y_v=-5
            x_v=x_v+2
        elif f.rect.y<=b.rect.y-20 and f.rect.y>b.rect.y-30:
            x_v=x_v+5
        elif f.rect.y<b.rect.y-30:
            y_v=y_v+5
            x_v=x_v+2
        wait=3
goal_bounce=False
def cross_bar(b,g):
    global y_v, x_v, goal_bounce
    if pygame.sprite.collide_rect(b,g):
        if b.rect.y<=g.rect.y+5:
            y_v=-(y_v)
        if b.rect.x>g.rect.x+10:
            if b.rect.y<=g.rect.y+5:
                x_v=-(x_v)
        goal_bounce=True
l=0
def x_move():
    global x_v
    game_ball.horz_move(x_v)
def check_wall():
    global x_v
    if x_v>0 and game_ball.rect.x>=950:
        x_v=-x_v
    if x_v<0 and game_ball.rect.x<=0:
        x_v=-x_v
y_v=0
def ball_gravity():
    global y_v
    if game_ball.rect.y!=300:
        y_v=y_v+1
def total_y_move():
    global y_v
    if game_ball.rect.y+50>=ground and y_v>0:
        y_v=(-y_v)+1
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
    global display_u_goal,display_o_goal, goal_bounce
    if game_ball.rect.x>=925 and game_ball.rect.y>=o_goal.rect.y and goal_bounce==False:
        display_u_goal=True
    if game_ball.rect.x<=25 and game_ball.rect.y>=user_goal.rect.y and goal_bounce==False:
        display_o_goal=True
    if goal_bounce==True:
        goal_bounce=False
move_up=False
move_down=False
move_left=False
move_right=False
foot_rotate= False
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
            if event.key == K_SPACE:
                foot_rotate=True
        if event.type==KEYUP:
            if event.key == K_UP:
                move_up=False
            if event.key == K_LEFT:
                move_left=False
            if event.key == K_RIGHT:
                move_right=False
            if event.key == K_SPACE:
                foot_rotate=False
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
    foot_r_x=0
    foot_r_y=0
    if foot_rotate==True:
        while foot_r_x<=20:
            foot_r_x=foot_r_x+1
            user_foot.rotation_out(foot_r_x,foot_r_y)
    if foot_rotate==False:
        while foot_r_x!=0:
            foot_r_x=foot_r_x-1
            user_foot.rotation_back(foot_r_x,foot_r_y)
    update(user)
    update(user_goal)
    update(o_goal)
    update(game_ball)
    user_foot.attatch(user.rect.x,user.rect.y,foot_r_x,foot_r_y)
    update(user_foot)
    foot_collision(user_foot,game_ball)
    collision(user,game_ball)
    cross_bar(game_ball,user_goal)
    cross_bar(game_ball,o_goal)
    x_move()
    check_wall()
    goal()
    total_y_move()
    if wait>0:
        wait=wait-1
    if display_o_goal==True:
        display_message('opponent goal',420,250, 32)
    if display_u_goal==True:
        display_message('user goal',430,250,32)
    pygame.display.update()
    fpsClock.tick(FPS)

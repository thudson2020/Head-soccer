import pygame, sys, time, random,math
from pygame.locals import *
from user import character
from goals import goals
from ball import ball
from foot import foot
from o_foot import o__foot
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("ball")
ground=350
BLACK=(0,0,0)
WHITE=(255,255,255)
FPS=60
x_v=0
fpsClock = pygame.time.Clock()

def update(x):
    DISPLAYSURF.blit(x.image,x.rect)
y_v=0
collision=False
wait=0
def collision(x,y):
    global x_v, y_v, wait
    if pygame.sprite.collide_rect(x,y) and wait==0:
        # y angle
        if x.rect.x+25>game_ball.rect.x+5:
            x_v=-5
        elif x.rect.x+25<= game_ball.rect.x+5 and x.rect.x> game_ball.rect.x+10:
            x_v=-4
        elif x.rect.x+25<= game_ball.rect.x+10 and x.rect.x> game_ball.rect.x+15:
            x_v=-3
        elif x.rect.x+25<= game_ball.rect.x+15 and x.rect.x> game_ball.rect.x+20:
            x_v=-2
        elif x.rect.x+25<= game_ball.rect.x+20 and x.rect.x> game_ball.rect.x+23:
            x_v=-1
        elif x.rect.x+25<= game_ball.rect.x+23 and x.rect.x> game_ball.rect.x+27:
            x_v=0
        elif x.rect.x+25<= game_ball.rect.x+27 and x.rect.x> game_ball.rect.x+30:
            x_v=1
        elif x.rect.x+25<= game_ball.rect.x+30 and x.rect.x> game_ball.rect.x+35:
            x_v=2
        elif x.rect.x+25<= game_ball.rect.x+35 and x.rect.x> game_ball.rect.x+40:
            x_v=3
        elif x.rect.x+25<= game_ball.rect.x+40 and x.rect.x> game_ball.rect.x+45:
            x_v=4
        elif x.rect.x+25<= game_ball.rect.x+45:
            x_v=5
        # x angle
        if x.rect.y+22<game_ball.rect.y+5:
            y_v=y_v-5
        elif x.rect.y+22>=game_ball.rect.y+5 and x.rect.y<game_ball.rect.y+10:
            y_v=y_v-4
        elif x.rect.y+22>=game_ball.rect.y+10 and x.rect.y<game_ball.rect.y+15:
            y_v=y_v-3
        elif x.rect.y+22>=game_ball.rect.y+15 and x.rect.y<game_ball.rect.y+20:
            y_v=y_v-2
        elif x.rect.y+22>=game_ball.rect.y+20 and x.rect.y<game_ball.rect.y+23:
            y_v=y_v-1
        elif x.rect.y+22>=game_ball.rect.y+23 and x.rect.y<game_ball.rect.y+27:
            y_v=y_v+0
        elif x.rect.y+22>=game_ball.rect.y+27 and x.rect.y<game_ball.rect.y+30:
            y_v=y_v+1
        elif x.rect.y+22>=game_ball.rect.y+30 and x.rect.y<game_ball.rect.y+35:
            y_v=y_v+2
        elif x.rect.y+22>=game_ball.rect.y+35 and x.rect.y<game_ball.rect.y+40:
            y_v=y_v+3
        elif x.rect.y+22>=game_ball.rect.y+40 and x.rect.y<game_ball.rect.y+45:
            y_v=y_v+4
        elif x.rect.y+22>=game_ball.rect.y+45:
            y_v=y_v+5
        wait=3
def foot_collision(f,b,m):
    global y_v, x_v, wait
    if pygame.sprite.collide_rect(f,b) and wait==0:
        if f.rect.y>b.rect.y-20:
            y_v=-(5*m)
            x_v=x_v+(2*m)
        elif f.rect.y<=b.rect.y-20 and f.rect.y>b.rect.y-30:
            x_v=x_v+(5*m)
        elif f.rect.y<b.rect.y-30:
            y_v=y_v+(5*m)
            x_v=x_v+(2*m)
        wait=3
goal_bounce=False
display_u_goal=False
display_o_goal=False
def cross_bar(b,g,gd):
    global y_v, x_v, goal_bounce, display_u_goal, display_o_goal, user_score, opponent_score
    if pygame.sprite.collide_rect(b,g):
        if b.rect.y<=g.rect.y+5:
            y_v=-(y_v)
        elif b.rect.x>g.rect.x+10:
            if b.rect.y<=g.rect.y+5:
                x_v=-(x_v)
        else:
            if gd==0:
                display_o_goal=True
                opponent_score=opponent_score+1
            else:
                display_u_goal=True
                user_score=user_score+1
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
user_score=0
opponent_score=0
def display_score():
    global user_score, opponent_score
    display_message('Player 1:'+str(user_score),5,5,16)
    display_message('Player 2:'+str(opponent_score),900,5,16)
move_up=False
move_down=False
move_left=False
move_right=False
foot_rotate= False
jump_time=0
o_move_up=False
o_move_down=False
o_move_left=False
o_move_right=False
o_foot_rotate= False
o_jump_time=0
PLAY=False
wait_gs=False
wait_gt=0
menue=True
rule=False
control=False
while True:
    DISPLAYSURF.fill(BLACK)
    if menue==True:
        display_message("HEADSOCCER",265,125,64)
        display_message("Play",450,200,42)
        display_message("Rules", 434,250,42)
        display_message("Controls", 407,300,42)
    if menue==False:
        pygame.draw.line(DISPLAYSURF, WHITE, (0, 350), (1000, 350), 4)
    for event in pygame.event.get():
        u_foot_rx=0
        u_foot_ry=0
        o_foot_rx=0
        o_foot_ry=0
        if menue==True:
            if event.type == MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                if position[0]>=450 and position[0]<=550 and position[1]>=200 and position[1]<=242:
                    PLAY=True
                    menue=False
                    user=character(ground,50)
                    opponent=character(ground, 900)
                    user_goal=goals(ground,0,0)
                    o_goal=goals(ground,950,1)
                    game_ball=ball(ground)
                if position[0]>=434 and position[0]<=466 and position[1]>=250 and position[1]<=292:
                    rule=True
                    menue=False
                if position[0]>=407 and position[0]<=493 and position[1]>=300 and position[1]<=342:
                    control=True
                    menue=False
        if PLAY==True and menue==False:
            if event.type== KEYDOWN:
                if(event.key==K_w):
                    move_up=True
                if event.key == K_a:
                    move_left=True
                if event.key == K_d:
                    move_right=True
                if event.key == K_SPACE:
                    foot_rotate=True
                if(event.key==K_UP):
                    o_move_up=True
                if event.key == K_LEFT:
                    o_move_left=True
                if event.key == K_RIGHT:
                    o_move_right=True
                if event.key == K_p:
                    o_foot_rotate=True
            if event.type==KEYUP:
                if event.key == K_w:
                    move_up=False
                if event.key == K_a:
                    move_left=False
                if event.key == K_d:
                    move_right=False
                if event.key == K_SPACE:
                    foot_rotate=False
                if event.key == K_UP:
                    o_move_up=False
                if event.key == K_LEFT:
                    o_move_left=False
                if event.key == K_RIGHT:
                    o_move_right=False
                if event.key == K_p:
                    o_foot_rotate=False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if PLAY==True and menue==False:
        user_foot=foot(user.rect.x,user.rect.y)
        o_foot=o__foot(opponent.rect.x,opponent.rect.y)
        if move_left==True and user.rect.x>=0:
            user.left()
        if move_right==True and user.rect.x<=950:
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
        if foot_rotate==True:
            while u_foot_rx<=20:
                u_foot_rx=u_foot_rx+1
                user_foot.rotation_out(u_foot_rx,u_foot_ry)
        if o_move_left==True and opponent.rect.x>=0:
            opponent.left()
        if o_move_right==True and opponent.rect.x<=950:
            opponent.right()
        if o_move_up==True:
            opponent.jump(o_jump_time)
            o_jump_time=o_jump_time+1
            if o_jump_time>18:
                o_jump_time=1
        if o_move_up==False:
            if o_jump_time!=0:
                opponent.jump(o_jump_time)
                o_jump_time=o_jump_time+1
            if o_jump_time>18:
                o_jump_time=0
        if o_foot_rotate==True:
            o_foot.rotation_out(opponent.rect.x,opponent.rect.y)
        if foot_rotate==False:
            while u_foot_rx!=0:
                u_foot_rx=u_foot_rx-1
                u_foot.rotation_back(u_foot_rx,u_foot_ry)
        if o_foot_rotate==False:
            o_foot.attatch(opponent.rect.x,opponent.rect.y)
        foot_collision(user_foot,game_ball,1)
        foot_collision(o_foot,game_ball,-1)
        collision(user,game_ball)
        collision(opponent,game_ball)
        cross_bar(game_ball,user_goal,0)
        cross_bar(game_ball,o_goal,1)
        x_move()
        check_wall()
        total_y_move()
        if wait>0:
            wait=wait-1
        if display_o_goal==True:
            display_message('opponent goal',420,250, 32)
            wait_gs=True
        if display_u_goal==True:
            display_message('user goal',430,250,32)
            wait_gs=True
        if wait_gs==True:
            PLAY=False
    if PLAY==False and menue==False:
        if display_o_goal==True:
            display_message('opponent goal',420,250, 32)
        if display_u_goal==True:
            display_message('user goal',430,250,32)
        x_v=0
        y_v=0
        wait_gt=wait_gt+1
        if wait_gt==50:

            move_up=False
            move_left=False
            move_right=False
            foot_rotate=False
            o_move_up=False
            o_move_left=False
            o_move_right=False
            o_foot_rotate=False
            o_display_o_goal=False
            display_u_goal=False
            if user_score==5:
                display_message("Player 1 wins", 400, 150, 32)
            if opponent_score==5:
                display_message("Player 2 wins", 400, 150, 32)
            user.rect.x=50
            user.rect.y=ground-44
            user_goal=goals(ground,0,0)
            o_goal=goals(ground,950,1)
            game_ball=ball(ground)
            user_foot=foot(user.rect.x,user.rect.y)
            o_foot=o__foot(opponent.rect.x,opponent.rect.y)
        if wait_gt==70:
            PLAY=True
            wait_gt=0
            wait_gs=False
            if user_score==5 or opponent_score==5:
                user_score=0
                opponent_score=0
                menue=True
                PLAY=False
                sprite.kill(user)
                sprite.kill(opponent)
                sprite.kill(foot)
                sprite.kill(o_foot)
                sprite.kill(user_goal)
                sprite.kill(o_goal)
                sprite.kill(game_ball)
    if menue==False:
        update(user)
        update(opponent)
        update(user_goal)
        update(o_goal)
        update(game_ball)
        user_foot.attatch(user.rect.x,user.rect.y,u_foot_rx,u_foot_ry)
        update(user_foot)
        update(o_foot)
        display_score()
    pygame.display.update()
    fpsClock.tick(FPS)

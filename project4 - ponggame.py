# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
start = False
paddle1_vel = 0
paddle2_vel = 0
acc=1
score1 = 0
score2 = 0
counter_time = 3
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2] 

    ball_vel = [-random.randrange(120,240)/60, random.randrange(60,180)/60*(random.randrange(0,2)*2-1)]
    if (direction == True):
        ball_vel = [random.randrange(120,240)/60, random.randrange(60,180)/60*(random.randrange(0,2)*2-1)]
        
# define event handlers
def new_game():
    global counter_time , ball_pos, ball_vel, start_game, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    counter_time = 3
    ball_pos = [WIDTH / 2, HEIGHT / 2] 
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    direction = random.random()<0.5

    spawn_ball(direction)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    timer.start()
    
    if (counter_time <1):
        timer.stop()
        # update ball
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]       
    
    
    # update paddle
    look = paddle1_pos + paddle1_vel
    look2 = paddle2_pos + paddle2_vel
    if ((look-HALF_PAD_HEIGHT >= 0) and (look + HALF_PAD_HEIGHT <= HEIGHT)): 
        paddle1_pos += paddle1_vel
   
    if ((look2-HALF_PAD_HEIGHT >= 0) and (look2 + HALF_PAD_HEIGHT <= HEIGHT)): 
        paddle2_pos += paddle2_vel
    
    # collide and reflect off of top side of canvas
    if ball_pos[1]>=HEIGHT-1-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # collide and reflect off of bottom side of canvas
    if ball_pos[1]<= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1] 
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles

    canvas.draw_line([HALF_PAD_WIDTH-1, paddle1_pos+HALF_PAD_HEIGHT], [HALF_PAD_WIDTH-1, paddle1_pos-HALF_PAD_HEIGHT], 8, 'Blue')
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH+1, paddle2_pos+HALF_PAD_HEIGHT], [WIDTH-HALF_PAD_WIDTH+1, paddle2_pos-HALF_PAD_HEIGHT], 8, 'Blue')
    
    # determine whether paddle and ball collide  
    
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if ((ball_pos[1] >= paddle1_pos-HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos+HALF_PAD_HEIGHT)):
                # collide and reflect off of left hand side of canvas
                ball_vel[0] = - ball_vel[0]
                ball_vel[0] = ball_vel[0] + ball_vel[0]*10/100
                ball_vel[1] = ball_vel[1] + ball_vel[1]*10/100
                
        
        else:
            score2 +=1
            spawn_ball(True)
   
    if ball_pos[0] >= WIDTH-BALL_RADIUS-PAD_WIDTH:
        if ((ball_pos[1] >= paddle2_pos-HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos+HALF_PAD_HEIGHT)):        
                # collide and reflect off of right hand side of canvas
                ball_vel[0] = - ball_vel[0]
                ball_vel[0] = ball_vel[0] + ball_vel[0]*10/100
                ball_vel[1] = ball_vel[1] + ball_vel[1]*10/100
        else:
            score1 +=1
            spawn_ball(False)
    
    # draw scores
    
    canvas.draw_text(str(score1),(WIDTH/4,100),40,'Red') 
    canvas.draw_text(str(score2),(WIDTH/4*3,100),40,'Red') 
    if ((counter_time <=3) and (counter_time >0)):
        canvas.draw_text(str(counter_time),[WIDTH/2-10,150],40,"Yellow")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 6    
    if key==simplegui.KEY_MAP["w"]: 
        look = paddle1_pos - (paddle1_vel-acc)
        paddle1_vel -= acc
       
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
        
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
       
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
       
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 6
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += acc

def count_down():
    global counter_time
    counter_time -= 1
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
timer = simplegui.create_timer(1000,count_down)
frame.set_draw_handler(draw)
frame.add_button("New Game",new_game,150)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()

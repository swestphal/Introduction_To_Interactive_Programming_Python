import simplegui

# define global variables
interval =  100
counter_time = 0
canvas_width = 600
canvas_height = 600
counter_tries = 0
counter_wins = 0
stop_check = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = int(t / 600)
    A = str(minutes)
    rest = t % 600
    
    seconds = int ( rest / 10)
    B = str("%02d" % seconds)
    rest2 = rest % 10
    
    milliseconds = rest2
    C = str(milliseconds)
    
    return str(A + ":" + B + "." + C)
    
# define helper function format x/y in appropriate string
def format_wins(x,y):
    try:
        percentage = (x * 100) / y
    except:
        percentage = 0
    win_string = str(x) + " / " + str(y) + " - " + str(percentage) + "% won"
    return win_string

# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    global stop_check
    stop_check = True
    timer.start()

def button_stop():
    global counter_wins
    global counter_tries
    global stop_check
    if (stop_check):
        if (counter_time % 10 == 0):
            counter_wins = counter_wins +1
        counter_tries = counter_tries +1
    stop_check = False
    timer.stop()

def button_reset():
    global timer
    global counter_time
    global stop_check
    global counter_wins
    global counter_tries
    stop_check = False
    counter_wins = 0
    counter_tries = 0
    timer.stop()
    timer = simplegui.create_timer(interval,tick)
    counter_time = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter_time
    counter_time = counter_time + 1
    
# define draw handler
def draw(canvas):
    counter_time_length = frame.get_canvas_textwidth(format(counter_time),100)
    canvas.draw_text(format(counter_time), [canvas_width/2-(counter_time_length/2),canvas_height/2+30],100,"Red")
  
    wins_length = frame.get_canvas_textwidth(format_wins(counter_wins,counter_tries),40)
    canvas.draw_text(format_wins(counter_wins,counter_tries),[canvas_width-wins_length-20,50],40,"Yellow")
# create frame
frame = simplegui.create_frame("Stopwatch",600,600)

# register event handlers
timer = simplegui.create_timer(interval,tick)
frame.add_button("Start",button_start,150)
frame.add_button("Stop",button_stop,150)
frame.add_button("Reset",button_reset,150)
frame.set_draw_handler(draw)

# start frame

frame.start()


import DotGL
import time
import random

#add "True" to use pixel width compensation
#if used use half the horizontal resolution you would
draw = DotGL.Screen(180,52)
#draw = DotGl.Screen(90, 52, True)

#draw.debug()


ball_x=0
ball_y=26
ball_x_momentum=1
ball_y_momentum=0
while(True):

    time.sleep(.01)
    draw.line(0,0,179,0)
    draw.line(179,0,179,51)
    draw.line(179,51,0,51)
    draw.line(0,51,0,0)
    
    if ball_x < 1:
        ball_x_momentum=1
        ball_y_momentum=random.triangular(-1,1,0)
    if ball_x > 178:
        ball_x_momentum=-1
        ball_y_momentum=random.triangular(-1,1,0)
    if ball_y < 1 or ball_y > 51: ball_y_momentum = ball_y_momentum *-1
    ball_x= ball_x + ball_x_momentum
    ball_y= ball_y + ball_y_momentum

    #both pixel and line can take an argument to change the character being used
    #this line() will make a line from the balls locaton to 0,0 and will use a "+" instead of the default "█"
    #draw.line(ball_x,int(ball_y),0,0, "+")
    draw.pixel(ball_x,int(ball_y))
    
    #draws the screen and manualy clears
    draw.update()
    draw.clear_screen() #not clearing can leave a trailing effect

    #other options
    #draws the screen and clears automaticly
    #draw.update(True)






    

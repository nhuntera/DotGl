import DotGL
import time
import random

width = 180
hight = 50

#add "True" to use pixel width compensation
#if used use half the horizontal resolution you would
draw = DotGL.Screen(width, hight)
#draw = DotGL.Screen(width, hight, True)

#draw.debug()


ball_x=0
ball_y=26
ball_x_momentum=1
ball_y_momentum=0
while(True):

    time.sleep(.03)
    draw.line(0,0,width-1,0)
    draw.line(width-1,0,width-1,hight-1)
    draw.line(width-1,hight-1,0,hight-1)
    draw.line(0,hight-1,0,0)
    
    if ball_x < 1:
        ball_x_momentum=1
        ball_y_momentum=random.triangular(-1,1,0)
    if ball_x > width-2:
        ball_x_momentum=-1
        ball_y_momentum=random.triangular(-1,1,0)
    if ball_y < 1 or ball_y > hight-1: ball_y_momentum = ball_y_momentum *-1
    ball_x= ball_x + ball_x_momentum
    ball_y= ball_y + ball_y_momentum

    #both pixel and line can take an argument to change the character being used
    #this line() will make a line from the balls locaton to 0,0 and will use a "+" instead of the default "█"
    #draw.line(ball_x,int(ball_y),0,0, "+")
    draw.pixel(int(ball_x),int(ball_y))
    
    #draws the screen and manualy clears
    draw.update()
    draw.clear_screen() #not clearing can leave a trailing effect

    #other options
    #draws the screen and clears automaticly
    #draw.update(True)






    

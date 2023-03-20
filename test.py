import DotGL
import time
import random

draw = DotGL.Screen(180,52,False)

draw.debug()


ballx=0
bally=26
ballxm=1
ballym=0
while(True):

    time.sleep(.01)
    draw.line(0,0,179,0)
    draw.line(179,0,179,51)
    draw.line(179,51,0,51)
    draw.line(0,51,0,0)
    
    if ballx < 1:
        ballxm=1
        ballym=random.triangular(-1,1,0)
    if ballx > 178:
        ballxm=-1
        ballym=random.triangular(-1,1,0)
    if bally < 1 or bally > 51: ballym = ballym *-1
    ballx= ballx + ballxm
    bally= bally + ballym
    #draw.line(ballx,int(bally),0,0)
    draw.pixel(ballx,int(bally))
    draw.update()

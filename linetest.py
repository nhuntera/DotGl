import DotGL
import time

draw = DotGL.screen(180,52,False)

draw.debug()


while(True):
    time.sleep(1)
    draw.line(0,10,0,15)
    #draw.update()
    draw.line(10,0,15,0)
    draw.line(52,5,32,41)
    draw.update()

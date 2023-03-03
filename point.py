import DotGL
import time
import random
from pynput import keyboard

draw = DotGL.screen(180,52,False)

draw.debug()


ballx=0
bally=26
ballxm=1
ballym=0
while(True):
    with keyboard.Events() as events:
        event = events.get(1e6)
        if event.key == keyboard.KeyCode.from_char('w'):
            ballx = bally + 1
        if event.key == keyboard.KeyCode.from_char('s'):
            ballx = bally - 1
        if event.key == keyboard.KeyCode.from_char('a'):
            bally = ballx - 1
        if event.key == keyboard.KeyCode.from_char('d'):
            bally = ballx + 1
    draw.pixel(ballx,bally)
    draw.update()
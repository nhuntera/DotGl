#████   █████  █████       █████  █
#█   █  █   █    █         █      █
#█   █  █   █    █         █  ██  █
#████   █████    █         █████  █████

#For the love of god dont use this (unless you really want to)
import os

class Screen:

    clear_string = "clear"

    #sets screen and innitalizes array
    def __init__(self, screen_width=180, screen_height=52,compensate=False): #compensate treates 2 chars like one pixel making the display wider per pixel
        
        self.compensate = compensate
        self.screenX = screen_width
        self.screenY = screen_height
        
        #populates the pixel array with spaces same as clear_screen()
        self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
        
        if os.name == 'nt':
            os.system(f'mode con: cols={screen_width*2} lines={screen_height+1}')
            self.clear_string = "cls"


    #draws new screen. If auto_clear is true the pixel array will also be cleared
    def update(self, auto_clear = False):

        os.system(self.clear_string)

        current_line = -1

        # compensates for the long shape of the "pixel" by treating two pixels as one
        if self.compensate:
            for line in self.__pixel_array:
               #clunky, but it sets current line to and increments it past that
                current_line = current_line+1
                for column in self.__pixel_array[current_line]:
                    print(column+column, end="")
                print("")
            if auto_clear:
                self.clear_screen()
        else:
            for line in self.__pixel_array:
               #clunky, but it sets current line to and increments it past that
                current_line = current_line+1
                for column in self.__pixel_array[current_line]:
                    print(column, end="")
                print("")
            if auto_clear:
                self.clear_screen()

    def clear_screen(self):
        
        self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]

    #place pixel in screen array at location
    def pixel(self, x, y, char="█"):
            
        xpos = x
        ypos = self.screenY-1-y
        
        self.__pixel_array[ypos][xpos] = char

    #draws a line using Bresenham's line algorithm
    def line(self, x0, y0, x1, y1, char="█"):
        
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.pixel(x, y, char)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.pixel(x, y, char)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
                
        self.pixel(x, y, char)

    #returns the char at poked location or "empty" if there is no pixel
    def poke_pixel(self, x, y):
        
        xpos = x
        ypos = self.screenY-1-y
        char = self.__pixel_array[ypos][xpos]
        
        if char == " ":
            return "empty"
        else:
            return char
    '''
    #bebug for testing screen
    def debug(self):
        toggel=1
        line = self.screenY
        lines = []
        for y in range(self.screenY):
                line = y
                lines.append(y)
                for x in range(self.screenX):
                    self.pixel(x,line)

        self.update()
        print(lines)
    '''

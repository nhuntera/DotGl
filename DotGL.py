#████   █████  █████       █████  █
#█   █  █   █    █         █      █
#█   █  █   █    █         █  ██  █
#████   █████    █         █████  █████

#For the love of god dont use this (unless you really want to)
import os

class screen:

    
    #sets screen and innitalizes array
    def __init__(self, screen_width, screen_height,compensate=False): #compensate treates 2 chars like one pixel (res:90x80)
        self.compensate = compensate
        self.screenX = screen_width
        self.screenY = screen_height
        if compensate:
            self.screenX = int(self.screenX/2)
            self.screenY = int(self.screenY/2)
        self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
        os.system(f'mode con: cols={screen_width} lines={screen_height}')
       
    #draws new screen  
    def update(self):
        os.system('cls')
        current_line = -1
        current_row = -1
        if self.compensate:
            for line in self.__pixel_array:
                current_line = current_line+1
                for row in self.__pixel_array[current_line]:
                    print(row*2, end="")
                print("")      
            self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
        else:
           for line in self.__pixel_array:
               current_line = current_line+1
               for row in self.__pixel_array[current_line]:
                   print(row, end="")
               print("")      
           self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
    
    def pixel(self, x, y):
            print(f"x:{x} y:{y}")
            x = int(x + self.screenX / 2)
            y = -int(y - self.screenY / 2)
            self.__pixel_array[y][x] = "█"
    
#    def slope_line(self, x=0, y=0, rise=1, run=1, length=1, comp=True): #my dumb and bad way of doing slope
#        rise = rise
#        posX = int(x)
#        posY = int(y)
#        if rise == 0 and comp:
#            length = length*2
#        for x in range(length):
#            self.pixel(posX, posY)
#            posX = posX + run
#            posY = posY + rise
            
    def draw_line(self, x1=0, y1=0, x2=0, y2=0): #I learned how to do math
        dx = abs(x2-x1)
        dy = abs(y2-y1)
        x = x1
        y = y1
        dx_pos = 1 if x1<x2 else -1
        dy_pos = 1 if y1<y2 else -1
        if dx==0:
            for x in range(dy):
                self.pixel(x,y)
                y = y+1
        else:
            if dx>dy:
                error = dx/2
                while x != x2:
                    self.pixel(x,y)
                    error = error - dx
                    if error < 0:
                        y = y+dy_pos
                        error = error + dx
                    x = x + dx
            else:
                error = dy/2
                while y != y2:
                    self.pixel(x,y)
                    error = error - dx
                    if error < 0:
                        x = x+dx_pos
                        error = error + dy
                    y = y + dy
        

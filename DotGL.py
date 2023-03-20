#████   █████  █████       █████  █
#█   █  █   █    █         █      █
#█   █  █   █    █         █  ██  █
#████   █████    █         █████  █████

#For the love of god dont use this (unless you really want to)
import os

class screen:


    #sets screen and innitalizes array
    def __init__(self, screen_width=180, screen_height=52,compensate=False): #compensate treates 2 chars like one pixel (res:90x80)
        self.compensate = compensate
        self.screenX = screen_width
        self.screenY = screen_height
        if compensate:
            self.screenX = round(self.screenX/2)
        self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
        os.system(f'mode con: cols={screen_width} lines={screen_height+1}')

    #draws new screen
    def update(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        current_line = -1
        if self.compensate:
            for line in self.__pixel_array:
                current_line = current_line+1
                current_row = -1
                for row in self.__pixel_array[current_line]:
                    current_row = current_row + 1
                    print((self.__pixel_array[current_line][current_row-1])*2, end="")
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
            xpos = x
            ypos = self.screenY-1-y
            if self.compensate:
                xpos=x-1
            #print(f"{xpos},{ypos}")
            self.__pixel_array[ypos][xpos] = "█"


    def line(self, x0, y0, x1, y1):
        #straight rip from Bresenham's line algorithm, sorry
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.pixel(x, y)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.pixel(x, y)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.pixel(x, y)
        

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

#████   █████  █████       █████  █
#█   █  █   █    █         █      █
#█   █  █   █    █         █  ██  █
#████   █████    █         █████  █████


import os

class screen:

    
    #sets screen and innitalizes array
    def __init__(self, screen_width, screen_height):
        self.screenX = screen_width
        self.screenY = screen_height
        self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
        os.system('mode con: cols=180 lines=52')
       
    #draws new screen  
    def update(self):
        os.system('cls')
        current_line = -1
        current_row = -1
        for line in self.__pixel_array:
            current_line = current_line+1
            for row in self.__pixel_array[current_line]:
                print(row, end="")
            print("")      
        self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
    
    def pixel(self, x, y):
        x = int(x + self.screenX / 2)
        y = -int(y - self.screenY / 2)
        self.__pixel_array[y][x] = "█"
    
    def slope_line(self, x=0, y=0, rise=1, run=1, length=1, comp=True): #my dumb and bad way of doing slope
        rise = rise
        posX = int(x)
        posY = int(y)
        if rise == 0 and comp:
            length = length*2
        for x in range(length):
            self.pixel(posX, posY)
            posX = posX + run
            posY = posY + rise

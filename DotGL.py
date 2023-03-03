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
            self.screenX = int(self.screenX/2)
            self.screenY = int(self.screenY)
        self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
        os.system(f'mode con: cols={screen_width} lines={screen_height}')
       
    #draws new screen  
    def update(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        current_line = -1
        current_row = 0
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
            #if x < 0:
            #    x = int(x + self.screenX / 2)
            #else:
            #    x = int(x + self.screenX / 2)-1
            #y = -int(y - self.screenY / 2)
            self.__pixel_array[-y][x] = "█"
    
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
  
    def line(self,x1,y1,x2,y2):
        dist_x = (x2-x1)
        dist_y = (y2-y1)
        x_direction = 1 if dist_x > 0 else -1
        y_direction = 1 if dist_y > 0 else -1
        if dist_x == 0: 
            while y1 != y2 and (0 <= y1 < self.screenX):
                self.pixel(int(x1),int(y1))
                y1 = y1+y_direction
            self.pixel(int(x1),int(y1))
        if dist_y == 0:
            while x1 != x2 and (0 <= x1 < self.screenX):
                self.pixel(int(x1),int(y1))
                x1 = x1+x_direction
            self.pixel(int(x1),int(y1))
        if dist_x > dist_y:
            pass
        if dist_x < dist_y:
            pass

    def debug(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        current_line = -1
        current_row = 0
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
                   print(current_line%10, end="")
               print("")      
           self.__pixel_array = [[" " for i in range(self.screenX)] for j in range(self.screenY)]
    
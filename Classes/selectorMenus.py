import keyboard
import os
from getch import pause
from playsound import playsound




#clears the screen
def clear():
    os.system("cls")

class menuInput:
    def __init__(self):
        self.selector = "> "
        self.listSelected = 1
       

    def printWrite(self, options):
        
        
        for x in range(len(options)):
           if x == self.listSelected:
               print(self.selector, options[x])
           else:
               print(options[x])
        pause('Press w or s to move up and down') 
        
        
    
    
    def write(self, options, soundPath):
        if keyboard.is_pressed("space"):
            return self.listSelected
        #self.printWrite(options)
        
        if keyboard.is_pressed("s") and self.listSelected + 1 < len(options):
            
            self.listSelected += 1
            playsound(soundPath, False)
            
        if keyboard.is_pressed("w") and self.listSelected -1 > 0:
            self.listSelected -= 1
            playsound(soundPath, False)
        clear()
        self.printWrite(options)
        
        
         
               
        
      
       
       
       
       
       
       
       









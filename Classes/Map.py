import copy
import os
import keyboard
import time
import sys
from os.path import exists
from termcolor import colored

#clears the screen
def clear():
    os.system("cls")



y = 0
x = 0



   


  

originMap = [
        ["F", "F", "F", "F", "F", "F", "S"],
        ["F", "F", "F", "F", "S", "S", "F"],
        ["F", "F", "S", "S", "F", "F", "F"],
        ["P", "S", "P", "C", "B", "B", "B"],
        ["M", "M", "H", "M", "B", "B", "B"]
    ]
  
map1 = [
        ["F", "F", "F", "F", "F", "F", "S"],
        ["F", "F", "F", "F", "S", "S", "F"],
        ["F", "F", "S", "S", "F", "F", "F"],
        ["P", "S", "P", "C", "B", "B", "B"],
        ["M", "M", "H", "M", "B", "B", "B"]
    ]

def applyColor(char):
    if char == "F":
        return colored("F", "green")
    else:
        return char
    

def mapPrint():
    global map1, y, x
    for row in map1:
        for col in row:
            print(applyColor(col), end=" ")
        print()
    print("X:",x, "Y:", y)


def mapMovement():
    global map1, y, x, wholeMenu, originMap
    
    
    map1[y][x] = "@"
    mapPrint()
    
    mapMovement1 = True
    while mapMovement1:
    
       
        
        if y == 4 and x == 2:
            map1[y][x] = "H"
            x -= 1
            map1[y][x] = "@"
            mapPrint()
            clear()
            return
        else:
            map1[y][x] = "@"
        
           
           
        map1 = copy.deepcopy(originMap)

        if  keyboard.is_pressed("w"):
            time.sleep(0.15)
            if y < len(map1):
                y -= 1 
                if y < 0:
                    y = 4
                

                map1[y][x] = "@"
                clear()
                mapPrint()
                
                
            else:
                
                y = 4
                y += 1
                map1[y][x] = "@"
                clear()
                mapPrint()


        if  keyboard.is_pressed("s"):
            time.sleep(0.15)
            y += 1 
            if y < len(map1):
                
                map1[y][x] = "@"
                clear()
                mapPrint()
                
            else:
                
                y = 0
                map1[y][x] = "@"
                clear()
                mapPrint()

        if  keyboard.is_pressed("a"):
            time.sleep(0.15)
            if x < len(map1[0]):
                x -= 1 
                if x < 0:
                    x = 6
                
                map1[y][x] = "@"
                clear()
                mapPrint()
            else:
                
                x = 6
                x -= 1
                map1[y][x] = "@"
                clear()
                mapPrint()
        if  keyboard.is_pressed("d"):
            time.sleep(0.15)
            x += 1 
            if x < len(map1[0]):
                
                map1[y][x] = "@"
                clear()
                mapPrint()
            else:
                
                x = 0
                map1[y][x] = "@"
                clear()
                mapPrint()
  


      

   
    
    
import os
#clears the screen
def clear():
    os.system("cls")
    

y = 0
x = 0
  

def originMapReset():
    global originMap
    originMap = [
        ["F", "F", "F"],
        ["F", "F", "F"],
        ["F", "F","F"],
        ["P", "P", "P"],
        ["M", "M", "M"]
        ]
  
map1 = [
        ["F", "F", "F"],
        ["F", "F", "F"],
        ["F", "F","F"],
        ["P", "P", "P"],
        ["M", "M", "M"]
    ]
def mapPrint():
    global map1
    for row in map1:
        for col in row:
            print(col, end=" ")
        print()
def mapRePrint():
    global originMap
    for row in originMap:
        for col in row:
            print(col, end=" ")
        print()
    
        
    

map1[y][x] = "@"
mapPrint()
mapMovement = True
while mapMovement:
    print("X:",x, "Y:", y)
    print("1. Up")
    print("2. Down")
    print("3. Left")
    print("4. Right")

    mapinput = input("# ")
    originMapReset()
    map1 = originMap
    
    if mapinput == "1":
        if y < len(map1):
            y -= 1 
            if y < 0:
                y = 4
            clear()
            
            map1[y][x] = "@"
            mapPrint()
        else:
            clear()
            y = 4
            y += 1
            map1[y][x] = "@"
            mapPrint()
        
            
            
            
            
            
            
    if mapinput == "2":
        y += 1 
        if y < len(map1):
            clear()
            map1[y][x] = "@"
            mapPrint()
        else:
            clear()
            y = 0
            map1[y][x] = "@"
            mapPrint()
            
    if mapinput == "3":
        if x < len(map1[0]):
            x -= 1 
            if x < 0:
                x = 2
            clear()
            map1[y][x] = "@"
            mapPrint()
        else:
            clear()
            x = 2
            x -= 1
            map1[y][x] = "@"
            mapPrint()
    if mapinput == "4":
        x += 1 
        if x < len(map1[0]):
            clear()
            map1[y][x] = "@"
            mapPrint()
        else:
            clear()
            x = 0
            map1[y][x] = "@"
            mapPrint()
   
    
    
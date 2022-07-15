import os
import random
import time
import math




#Main Gamemodes
adventure = False
home = False

#home submenus
inAnvil = False
inForge = False
inChest = False

#menus
mainmenu = True

#Home Improvments
anvil = False
forge = False
chest = False
loom = False
horse = False

#Adventuring
advNorth = False
advSouth = False
advEast = False
advWest = False

#Town
town = False
mine = False
shop = False


#Stats
gold = 0
health = 20
dmg = 1

def clear():
    os.system("cls")

#Main Menu
while mainmenu:
    print("Welcome to Python Text Based Adventure")
    print("1. Play Game")
    print("2. Credits")
    print("3. Exit")
    menuinput = input("# ")
    clear()
#main menu choices
    if menuinput == "1":
        home = True
        mainmenu = False
    elif menuinput == "2":
        print("Creator: Max Warren")
        print("Coder: Max Warren")
    elif menuinput == "3":
        quit()
    
#Home
while home:
    print("This is your home!")
    print("1. Go out Adventuring")
    if anvil == True:
        print("2. Use your anvil")
    if forge == True:    
        print("3. Use your forge")
    if chest == True:
        print("4. Open your chest")
    print("5. Go to Town")
    homeinput = input("# ")
    clear()
    
    
    
    #Adventuring
def begginingAdventure():
    if adventure == True:
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        advinput = input("# ")
        clear()
    
    if advinput == "1":
        advNorth = True
        adventure = False
        print("you decided to go North")
    if advinput == "2":
        advSouth = True
        adventure = False
        print("you decided to go South")
    if advinput == "3":
        advEast = True
        adventure = False
        print("you decided to go East")
    if advinput == "4":
        advWest = True
        adventure = False
        print("you decided to go West")
    else:
        print("invalid input")
        begginingAdventure()
        clear()
        
        
    
if advNorth == True:
    print("while traveling north you come a across a Cave \n do you go in the cave? or do you pass by it?")
    print("1. Enter the Cave")
    print("2. Pass the Cave")
    northinp = input("# ")
    clear()
    
    if northinp == "1":
        
        print("You enter the cave and ")
    if northinp == "2":
        print("You go around the cave and you come to a fork \n do you go left or right?")
    
    
    
    
    
    #Home Choices
    if homeinput == "1":
        adventure = True
        home = False
        begginingAdventure()
    if homeinput == "2" and anvil == True:
        pass
    elif homeinput == "2" and anvil == False:
        print("You havent unlocked that yet")
    if homeinput == "3" and forge == True:
        pass
    elif homeinput == "3" and forge == False:
        print("You havent unlocked that yet")
    if homeinput == "4" and chest == True:
        pass
    elif homeinput == "4" and chest == False:
        print("You havent unlocked that yet")
    if homeinput == "5":
        town = True
        
while town:
    print("Test")
    print("Test2")
        
        
        
        


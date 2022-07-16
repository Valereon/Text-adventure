import os
import random

import time
import math
from unittest import result
import decsions
from decsions import *



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


    
        
def encounter():
    mathencounter = 3
    if mathencounter == 10:
        pass
    if mathencounter == 9:
        pass
    if mathencounter == 8:
        pass
    if mathencounter == 7:
        pass
    if mathencounter == 6:
        pass
    if mathencounter == 5:
        pass
    if mathencounter == 4:
        pass
        
    
    if mathencounter == 3:
        adventure = False
        d3 = decsions.decsion("on your travels you stumble upon a cave do you enter?", "1. Yes", "2. No")
        result3 = d3.pts
        
        if d3 == "1":
            d3_1_1 = decsions.decsion.pts("As you walk into the cave you encounter a horde of monsters! do you fight or runaway?", "1. Fight", "2. Run Away")
            
            
        if d3 == "2":
            adventure = True
            
    if mathencounter == 2:
        pass
    if mathencounter == 1:
        pass
    
         

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
    
#Home Choices
    if homeinput == "1":
        adventure = True
        home = False
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
    

    
    #Adventuring
    while adventure == True:
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        advinput = input("# ")
        clear()
    
        if advinput == "1":
            print("you decided to go North") 
            encounter()
        elif advinput == "2":           
            print("you decided to go South")
            encounter()
        elif advinput == "3":         
            print("you decided to go East")
            encounter()
        elif advinput == "4":
            print("you decided to go West")
            encounter()
        else:
            clear()
            print("invalid input")
       
        

    
    
    
    
        
while town:
    print("Test")
        



        
        


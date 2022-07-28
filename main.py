import os
import random
from os.path import exists
from getch import pause

from Classes.decsions import decsion
from Classes.enemy import monster
from Classes.human import player
from Classes.Loot import *
from Classes.selectorMenus import menuInput
from Classes.Map import *
from Classes.Map import mapMovement



#Main Gamemodes

home = False
battle = False

#home submenus
inAnvil = False
inForge = False
inChest = False

#menus
mainmenu = True
saveCreated = False

#Home Improvments
anvil = False
forge = False
chest = False


#Town
town = False
mine = False
shop = False
generator = False



#Stats
usedskillpoints = 0
unusedskillpoints = 0
playerLvl = 1
xp = 0
maxLevel = 50
xpNeeded4NextLevel = 10    
    

    
    
#declaring the  player    
player1 = player()    
mainmenu1 = menuInput()
homemenu = menuInput()
generalMenu = menuInput()
#clears the screen
def clear():
    os.system("cls")
    
#leveling up the player
def levelUp():
    global playerLvl, xpNeeded4NextLevel, unusedskillpoints
    unusedskillpoints += 1
    if playerLvl <= 50:
        playerLvl += 1
    xpNeeded4NextLevel *= random.randint(2,5)
        
#the skillpoint upgrade screen        
def skillPointScreen():
    global unusedskillpoints, home
    while skillPointScreen:
        clear()
        print("You Have " + str(unusedskillpoints) + " Unused Skillpoints!")
        print("1. Max Health + 5")
        print("2. Attack + 1")
        print("3. Defense + 1")
        print("4. Luck + 1")
        skillpointinput = input("# ")
        clear()
        if unusedskillpoints >= 1:
            if skillpointinput == "1":
                player1.maxhealth += 5
                unusedskillpoints -= 1
                continue
            elif skillpointinput == "2":
                player1.attack += 1
                unusedskillpoints -= 1
                continue
            elif skillpointinput == "3":
                player1.defense += 1
                unusedskillpoints -= 1
                continue
            elif skillpointinput == "4":
                player1.luck += 1
                unusedskillpoints -= 1
                continue
        if skillpointinput == "x":
                home = True
                return
                
                

def inventoryScreen():
    player1.openInventory()
    input("# ")
    clear()

def equippedScreen():
    pass

def profile():
    global home
    while profile:
        print(str(player1.maxhealth) + " Max Health")
        print(str(player1.health) + " Health")
        print(str(player1.attack) + " Attack")
        print(str(player1.defense) + " Defense")
        print(str(player1.luck) + " Luck")
        print("")
        print("1. Open Skill Menu")
        print("2. Open Your Inventory")
        print("3. Open Your Equipped")
        profileMenuInput = input("# ")
        clear()

        if profileMenuInput == "1":
            skillPointScreen()    
        if profileMenuInput == "2":
            inventoryScreen()
        if profileMenuInput == "3":
            equippedScreen()
        if profileMenuInput == "x":
            home = True
            return
            
        
        
        
    
def save():
    file_exists = exists("Save.txt")
    if file_exists == True:
        saveList = [
            str(playerLvl),
            str(xp),
            str(xpNeeded4NextLevel),
            str(player1.maxhealth),
            str(player1.health),
            str(player1.attack),
            str(player1.defense),
            str(player1.luck),
            str(unusedskillpoints),
            str(y),
            str(x)
            
        ]   
        saveFile = open("Save.txt", "w")
        for item in saveList:
            saveFile.write(item + "\n")
        saveFile.close    
    if file_exists == False:
        saveFile = open("Save.txt", "x")
        print("Save File Created. Save Again To save your progress!")
    
    
    
        
    





#when you die this appears
def deathscreen():
    global adventure, home
    clear()
    print("you lost everything beseides equipped items")
    print("You died press enter to go back to town")
    adventure = False
    home = True
    input("# ")
    
#the battling function
def fight():
    global xp, xpNeeded4NextLevel, playerLvl, monster1
    battle = True
    monster1 = monster(playerLvl)
    monster1.statreset()
    while battle:
        print("Monster Health:", monster1.health)
        print("Monster Attack:", monster1.attack)
        print("")
        print("Your Health:", player1.health)
        print("Your Attack:", player1.attack)
        print("Your Defense:", player1.defense)
        print("1. Attack")
        print("2. Potion")
        print("3. Open your Bag")
        print("4. Flee (Chance to Fail)")
        attackinput = input("# ")
        clear()
        
        #choices
        if attackinput == "1":
            monster1.health -= player1.attack
            if monster1.health <= 0:
                battle = False
                xp += monster1.xp
                monster1.statincrease(playerLvl)
                print("You win!")
                print("You Gained " + str(monster1.xp) + " Exp")
                print(monster1.monsterDrops())
                if xp >= xpNeeded4NextLevel:
                    levelUp()
                    print("You Leveled up! You are now Level", playerLvl)
                    print("+1 Skillpoint")
                
                #print(loot)
                input("# ")
                battle = False
               
        if attackinput == "2":
            pass
        if attackinput == "3":
            player1.openbag()
        if attackinput == "4":
            fleechance = random.randint(1,100)
            if fleechance <= 25:
               
                battle = False

       
        #making sure the monster dosent attack you after you win
        if attackinput != "3" and monster1.health >= 1:
        #randomizing attack or potion
            monsterRando = random.randint(1,15)
            if monsterRando >= 13:
                monster1.health += random.randint(5,10)
                clear()
                print("The monster drank a potion!")
                input("> ")
    
            if monsterRando <= 12:
                defenseRandom = random.randint(1,100)
                
                #if defense is active then reduce monster attack
                if defenseRandom <= player1.defense:
                    defenseattack = monster1.attack 
                    defenseattack -= player1.defense
                    
                    if defenseattack <= 1:
                        defenseattack = 1
                    player1.health -= defenseattack
                    clear()
                    
                    print("The monster attacked you!")
                    print("But you Defended! and took less damage!")
                    input("> ")
                    
                else:
                    clear()
                    print("The monster attacked you!")
                    player1.health -= monster1.attack
                    input("> ")


       #story encounters when your picking your direction 

    global home
    mathencounter = 3 #random.randint(1,10)
    if mathencounter == 10:
        d10 = decsion("You found Home!", "1. Enter your house", "2. continue adventuring")
        result10 = d10.pts()
        clear()
        
        if result10 == "1":
            home = True
        if result10 == "2":
            pass
        

#Main Menu
while mainmenu:
    def printMainMenu():
        global mainMenuResult1
        mainMenuResult1 = mainmenu1.write(["Welcome to Not another text adventure!", "New Game", "Load Game", "Credits", "Quit"], "H:\\Github\\GitHub\\Text-adventure\\soundEffectsAndMusic\\menuselect.wav")
    printMainMenu()    
    
    
        #main menu choices
    if mainMenuResult1 == 1:
        home = True
        mainmenu = False
        
    elif mainMenuResult1 == 2:
        try:
            saveFile = open("Save.txt")
            loadList = saveFile.readlines()
            if len(loadList) == 9:
                playerLvl  = int(loadList[0][:-1])
                xp = int(loadList[1][:-1])
                xpNeeded4NextLevel = int(loadList[2][:-1])
                player1.maxhealth = int(loadList[3][:-1])
                player1.health = int(loadList[4][:-1])
                player1.attack = int(loadList[5][:-1])
                player1.defense = int(loadList[6][:-1])
                player1.luck = int(loadList[7][:-1])
                unusedskillpoints = int(loadList[8][:-1])
                home = True
                mainmenu = False
            else:
                print("Save Is corrupted")
                input("> ")
        except OSError:
            print("No loadable file!")
            input("> ")
            
    elif mainMenuResult1 == 3:
        print("Creator: Max Warren")
        print("Coder: Max Warren")
        printMainMenu()
    elif mainMenuResult1 == 4:
        quit()
#Home
while home:
    def printHomeMenu():
        global homeMenuResult
        homeMenuResult = homemenu.write(["This is your home!", "Go out adventuring", "use your anvil", "use your forge", "open your chest", "go to town", "open your profile", "Save"], "H:\\Github\\GitHub\\Text-adventure\\soundEffectsAndMusic\\menuselect.wav")  
    printHomeMenu()
    pause("Press w or s to move up or down!")
    
    if unusedskillpoints >= 1:
        print("You have " + str(unusedskillpoints) + " Unused Skillpoints!")
    
#Home Choices
    if homeMenuResult == 1:
        result = mapMovement()
    if homeMenuResult == 2 and anvil == True:
        pass
    elif homeMenuResult == 2 and anvil == False:
        print("You havent unlocked that yet")
        printHomeMenu()
    if homeMenuResult == 3 and forge == True:
        pass
    elif homeMenuResult == 3 and forge == False:
        print("You havent unlocked that yet")
        printHomeMenu()
    if homeMenuResult == 4 and chest == True:
        pass
    elif homeMenuResult == 4 and chest == False:
        print("You havent unlocked that yet")
        printHomeMenu()
    if homeMenuResult == 5:
        town = True    
    if homeMenuResult == 6:
            profile()
    if homeMenuResult == 7:
        save()
        printHomeMenu()

  
    

        
        
    

    
    
    
        
while town:
    print("Test")
        



        
        


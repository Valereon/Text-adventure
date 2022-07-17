
import os
import random
import time
import math




from Classes.decsions import decsion
from Classes.enemy import monster
from Classes.human import player




#Main Gamemodes
adventure = False
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
unusedskillpoints = 1
playerLvl = 1
xp = 0
maxLevel = 50
xpNeeded4NextLevel = 10    
    
#declaring the  player    
player1 = player()    

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
    global unusedskillpoints
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
                profile()

def inventoryScreen():
    player1.openInventory()
    input("# ")
    clear()

def equippedScreen():
    pass

def profile():
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
    global adventure, xp, xpNeeded4NextLevel, playerLvl
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
                adventure = True
                xp += monster1.xp
                monster1.statincrease(playerLvl)
                print("You win!")
                print("You Gained " + str(monster1.xp) + " Exp")
                if xp >= xpNeeded4NextLevel:
                    levelUp()
                    print("You Leveled up! You are now Level", playerLvl)
                    print("+1 Skillpoint")
                
                #print(loot)
                input("# ")
                battle = False
                adventure = True
        if attackinput == "2":
            pass
        if attackinput == "3":
            player1.openbag()
        if attackinput == "4":
            fleechance = random.randint(1,100)
            if fleechance <= 25:
                adventure = True
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
def encounter():
    global home, adventure
    mathencounter = 3 #random.randint(1,10)
    if mathencounter == 10:
        d10 = decsion("You found Home!", "1. Enter your house", "2. continue adventuring")
        result10 = d10.pts()
        clear()
        
        if result10 == "1":
            home = True
            adventure = False
        if result10 == "2":
            adventure = True
        
        
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
        d3 = decsion("on your travels you stumble upon a cave do you enter?", "1. Yes", "2. No")
        result3 = d3.pts()
        
        if result3 == "1":
            clear()
            d3_1_1 = decsion("As you walk into the cave you encounter a horde of monsters! do you fight or runaway?", "1. Fight", "2. Run Away")
            result3_1 = d3_1_1.pts()
            
            
            if result3_1 == "1":
                clear()
                fight()
                #fight the monsters
                pass
            
            if result3_1 == "2":
                clear()
                d3_2_2 = decsion("You run off the right deeper into the cave and come across a fork", "1. Go Left", "2. Go Right")
                result3_2 = d3_2_2.pts()
                
                if result3_2 == "1":
                    clear()
                    print("You found a chest with lots of loot in it the loot is") # make chest loot here
                    
                if result3_2 == "2":
                    clear()
                    d3_3_2 = decsion("you go right and you find a chest guarded by monsters", "1. Fight", "2. Accept your fate")
                    result3_3 = d3_3_2.pts()
                    
                    if result3_3 == "1":
                       clear()
                       fight()
                    
                    if result3_3 == "2":
                        deathscreen()  
            
        if result3 == "2":
            adventure = True
            
    if mathencounter == 2:
        clear()
        d2 = decsion("as your walking along you stumble across a beached boat do you enter?", "1. Yes", "2. No")
        result2 = d2.pts()
        
        if result2 == "1":
            clear()
            d2 = decsion("You enter the boat and you see a group of skeletons sitting around a fire what do you do?", "1. Attack them", "2. Chat with them" )
            result2 = d2.pts()
            
            if result2 == "1":
                clear()
                fight()
                #attack here
                
            if result2 == "2":
                clear()
                d2 = decsion("you apporach the group of skeletons with a swagger and they seem to vibe with it one gets up and stares you in the eyes what do you do?", "1. dance battle", "2. rap battle")
                result2 = d2.pts()
                
                if result2 == "1":
                    clear()
                    d2 = decsion("you start BUSTING A MOVE as hard as you can the skeleton dosent even miss a beat he starts Breakdancing and the others start cheering it seems like they are cheering for you more", "1. do a flip", "2. Stop and ask for a large sum of cash")
                    result2 = d2.pts()
                    if result2 == "1":
                        clear()
                        d2 = decsion("You execute a perfect backflip and blow away the crowd", "1. ask for the chest in the back", "2. leave with their thanks")
                        result2 = d2.pts()
                        
                        if result2 == "1":
                            pass
                        if result2 == "2":
                            pass
                    if result2 == "2":
                        pass
                        
                if result2 == "2":
                    clear()
                    d2 = decsion("you start rapping harder than eminem and they are impressed, the one in front of you dosent even blink before he starts rapping 1000x faster than you. Its barely comprehendable what do you do?", "1. rap faster", "2. start breakdancing")
                    result2 = d2.pts()
                    
        if result2 == "2":
            adventure = True
    if mathencounter == 1:
        pass
    
         

#Main Menu
while mainmenu:
    print("Welcome to Python Text Based Adventure")
    print("1. New Game")
    print("2. Load Game")
    print("3. Credits")
    print("4. Exit")
    menuinput = input("# ")
    clear()
#main menu choices
    if menuinput == "1":
        home = True
        mainmenu = False
        if saveCreated == False:
            save = open("Save.txt", "x")
        elif saveCreated == True:
            save = open("Save.txt")
        
    elif menuinput == "2":
        pass
    elif menuinput == "3":
        print("Creator: Max Warren")
        print("Coder: Max Warren")
    elif menuinput == "4":
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
    print("6. Open your Profile")
    if unusedskillpoints >= 1:
        print("You have " + str(unusedskillpoints) + " Unused Skillpoints!")
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
    if homeinput == "6":
            profile()

    
    #Adventuring
    while adventure:
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
        



        
        


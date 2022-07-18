import random

from .human import *
class monster:
    def __init__(self, playerLvl):
        self.health = playerLvl + random.randint(1, 15)
        self.maxhealth = self.health
        self.attack = playerLvl + random.randint(1, 5)
        self.xp = playerLvl + random.randint(5, 20)
       
    def statincrease(self, playerLvl):
        
        self.maxhealth += random.randint(1, 15)
        self.attack += random.randint(1,10)
        self.xp += playerLvl * 2
    
    def statreset(self):
        self.health = self.maxhealth
    
    def monsterDrops(self):
        
        lootDrops = [
            ["Limb", "Guts", "Fang", "Horn", "Eye", "Iron Nugget", "Stick", "Rock", "Scale", "Claw"],
            ["Dagger", "Sword", "Iron Ingot", "Gold", "Silver", "Spear", "Mace"],
            ["Ring Of Life", "Ring of Thunder", "Potion", "Amulet of Protection"]
        ]
        
        lootListSelection = random.choices(lootDrops, weights=[60, 30, 10], k=1)   
        
        lootDropsLen = len(lootDrops)  

        lootDecsion2 = lootListSelection[0][random.randint(0, lootDropsLen-1)]
        player1 = player()
        player1.addItemToInventory(lootDecsion2)

        
 
        
        print(lootDecsion2)
        
        
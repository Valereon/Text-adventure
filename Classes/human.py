

from numpy import number


class player:
    def __init__(self):
        self.health = 10
        self.maxhealth = self.health
        self.attack = 5
        self.defense = 5
        self.luck = 1
        self.gold = 0
        
    def inventorymethod(self):
        self.inventory = []
        self.equippedinventory = []
        self.bag = []
       
    def openbag(self):
        self.inventorymethod()
        number = 0
        for i in self.bag:
            number += 1
            print(str(number) + ". " + i)
        print("Which one would you like to use?")
        input("# ")
        
    def addItemToInventory(self, itemName):
        self.inventorymethod()
        self.inventory.append()
    
    def openInventory(self):
        self.inventorymethod()
        number1 = 0
        for x in self.inventory:
            number1 += 1
            print(str(number1) + ". " + x)
            
        
import random




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
        pass
        
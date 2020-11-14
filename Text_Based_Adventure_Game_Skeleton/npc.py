class npc:
    def __init__(self,currentHealth = 3,damage = 1,maxHealth = 3,alive = True):
        self.currentHeath = currentHealth
        self.maxHealth = maxHealth
        self.damage = damage
        self.alive = alive
     
         
    #getter and setter for current Health     
    def setCurrentHealth(self,value):
        self.currentHealth = value

    def getCurrentHealth(self):
        return self.currentHealth


    #getter and setter for maxHealth
    def setMaxHealth(self,value):
        self.maxHealth = value

    def getMaxHealth(self):
        return self.maxHealth


    #getter and setter for the damage the npc does
    def setDamage(self,value):
        self.damage = value    

    def getDamage(self):
        return self.damage  


    #getter and setter for the boolean value alive
    def setAlive(self,boolVal):
        self.alive = boolVal     

    def getAlive(self):
        return self.alive


    #for damaging the npc 
    def takeHealth(self,change):
        if((self.currentHealth - change) <= 0):
            self.setAlive(False)
        else:
            self.currentHealth -= change      
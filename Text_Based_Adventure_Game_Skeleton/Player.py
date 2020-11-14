import time
import random

class Player:

    def __init__(self,name = "",currentHealth = 10,maxHealth = 10, damage = 1):
        self.name = name
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.damage = damage
       


    #getter and setter for name
    def setName(self,value):
        self.name = value

    def getName(self):       
        return self.name

         
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


    #getter and setter for the damage the player does
    def setDamage(self,value):
        self.damage = value    

    def getDamage(self):
        return self.damage

    #is called when the player is at or below 0 current HP
    #they will roll a d6 (1-3 they die, 4-6 they live)
    #if the live their current health is set to 1 
    #and max HP is reduced by 1
    def deathsDoor(self,currentHealth,maxhealth):        
        diceRoll = random.randint(1,6)
        print("You are now on deaths door\n"
              "Your life hangs in the balance...\n")
        time.sleep(1.5)
        if(diceRoll < 4):
            print("And with a shudder you collapse\n"
                            "DEAD\n")
            time.sleep(3.5) 
        #The player dies and the game exits                    
            exit()                
        else:                    
            print("You barely hold on to life\n"
                  "But you are forever scarred\n")

            time.sleep(1.5)      
            #The player lives, their max health is reduced by 1 if it is not already that and they are placed back at 1 hp
            maxHealth = self.getMaxHealth()
            if(maxHealth > 1):
                self.setMaxHealth(maxHealth - 1)
            self.setCurrentHealth(1)

            print(self.currentHealth)
            print(self.maxHealth)

    #for healing the player
    def giveHealth(self,change):
        if((self.currentHealth + change) > self.maxHealth):
            self.currentHealth = self.maxHealth
        else:
            self.currentHealth += change        
        

    #for damaging the player and checking if on deaths door
    def takeHealth(self,change):
        if((self.getCurrentHealth() - change) <= 0):
            #player is dead and needs to do a deaths door check
            self.deathsDoor(self.getCurrentHealth,self.getMaxHealth)
        else:
            self.currentHealth -= change



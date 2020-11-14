import Player
import npc
import time

#possible user responses
answerA = ["a","A"]
answerB = ["b","B"]
answerC = ["c","C"]
answerD = ["d","D"] 
yes = ["y","yes","YES"]
no = ["n","no","NO"]

#If no correct input is selected from the availabe choices
inputError = ("\nPlease Choose a Correct Answer\n")

#Initiliaze the player and a goblin for them to fight
myPlayer = Player.Player("Alex",10,10,1)
goblinNPC = npc.npc(3,1,3,True)



####THE START OF THE GAME####
def intro():
    print("This is where the introduction of the game would begin. Usually it would include"
          "some sort of BACKSTORY. However, as this is just a test / template i will leave"
          "it blank for the most part.\n\n"
          
          "A.) This choice takes you to method A\n"
          "B.) This choice takes you to method B\n"
          "C.) This choice takes you to method C\n")

    time.sleep(2)
    choice = input(">>>")

    #choice A
    if choice in answerA:
        optionA()
    #choice B    
    elif choice in answerB:
        optionB()
    #choice C    
    elif choice in answerC:
        optionC()
    #no correct choice was made, print error and restart intro method    
    else:
        print(inputError)
        intro()  


#choice from A
def optionA():
    print("this is the resulting choice from option A\n"
          "hurting the player for 2 damage\n")
    myPlayer.takeHealth(2)
    print(myPlayer.getCurrentHealth())

#choice from Babb
def optionB():
    print("this is the resulting choice from option B\n"
          "Hurting the player for 10 and putting them on\n"
          "Deaths Door\n")
    myPlayer.takeHealth(10)      

#choice from C
def optionC():
    print("this is the resulting choice from option C\n"
          "Nothing happens :)\n")    



#call the intro method
intro()    
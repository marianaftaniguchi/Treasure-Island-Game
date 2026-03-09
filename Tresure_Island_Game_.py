print ('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 

''')

print("Welcome to Treasure Island.")

print("Your mission is to find the treasure.")

print ("You're at a cross road. Where you want to go?")

a = input ('Type "left" or "right": ')

if a == "right":

    print ("You fell into a hole. Game over")

else: 

    print ("You've come to a lake. There is an island in the middle of the lake")

    b = input ('Type "wait" to wait to the boat. Type "swim" to swim across: ')

    if b == "swim":
    
     print ("You get attacked by trout. Game over.")

    else:

     print ("You arrive at the island unharmed. There is a house with 3 doors.")

     c = input ('One red, one blue and one yellow. Which color do you choose? ')

     if c == "red":
     
        print ("It's a room of fire. Game Over.")

     elif c == "blue":
     
        print ("You enter a room of beasts. Game over.")

     elif c == "yellow":
        
        print ("Congratulations! You won the game!")

     else: 
        
        print ("Game Over!")



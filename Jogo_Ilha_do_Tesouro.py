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

print("Seja bem-vindo(a) ao jogo da Ilha do Tesouro!")

print("A sua missão é encontrar o tesouro.")

print ("Você está em um cruzamento. Para qual lado deseja ir?")

a = input ('Escreva "esquerda" ou "direita": ')

if a == "direita":

    print ("Você caiu em um buraco! Game Over.")

else: 

    print ("Você chegou até um lago. Tem uma olha no meio desse lago.")

    b = input ('Escreva "esperar" para esperar um barco. Escreva "nadar" caso queira nadar até a ilha: ')

    if b == "nadar":
    
     print ("Você foi atacado por trutas! Game over.")

    else:

     print ("Você chegou em uma ilha estranha. Lá, há uma casa com 3 portas coloridas.")

     c = input ('Uma vermelha, uma azul e uma amarela. Qual cor você escolhe? ')

     if c == "vermelha":
     
        print ("O local está pegando fogo! Game over.")

     elif c == "azul":
     
        print ("É um local com inúmeras bestas! Game over.")

     elif c == "amarela":
        
        print ("Parabéns! Você encontrou o tesouro!")

     else: 
        
        print ("Game Over!")

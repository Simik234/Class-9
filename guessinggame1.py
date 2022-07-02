from random import *

I = 0
while I < 5:
    randomNumber = randint(1, 9)
    number = input("Guess a number between 1 to 9: ")
    a = int(number)
    if a == randomNumber:
        print("You win")
        break
    else:
        print("You lose")
    print(number)
    print(randomNumber)
    I = I + 1
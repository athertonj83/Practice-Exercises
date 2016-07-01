#ex09 guessing game
import random

#random number between 1-9 (inclusive)
num=random.randrange(1,10)
count=0
guess=0

while int(guess)!=num:
    guess=input("Please guess a number between 1 and 9: ")
    count+=1

    if guess=="exit":
        print("Quitting? Ok. The number was:",num)
        break

    if int(guess)==num:
        print("Well done, you guessed correct!")
        print("Number of guesses:",count)

    elif int(guess)<num:
        print("Too low, try again.")
        continue
    elif int(guess)>num:
        print("Too high, try again.")
        continue
    else:
        print("Second continue")

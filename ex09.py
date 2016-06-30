#ex09 guessing game
import random

#random number between 1-9 (inclusive)
num=random.randrange(1,10)
count=1

guess=input("Please guess a number between 1 and 9: ")

while ((guess.isdigit() and guess!=num) or (guess=="exit")):

    if not guess.isdigit() and guess=="exit":
        print("Quitting? Ok. The number was:",num)
        break

    if int(guess)==num:
        print("Well done, you guessed correct!")
        print("Number of guesses:",count)
        break

    elif int(guess)<num:
        print("Too low, try again.")
    else:
        print("Too high, try again.")

    guess=input("Please guess another number between 1 and 9: ")
    count+=1
    continue

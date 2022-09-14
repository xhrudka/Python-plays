from ast import If
import random

roll=random.randint(1,6)

guess=int(input("Guess the dice roll:\n"))

if guess==roll:
    print("Correct the random number is: " +str(roll))
else:
    print("Wrong! The number was " +str(roll))
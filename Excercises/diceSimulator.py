"""

Excercise in the chapter 3.14 

This project simulates a dice roll by generating a random number between 1 and 6. 
Each time the program runs, it "rolls the dice" and displays the result. 
his project introduces students to working with random numbers and basic output formatting

/------------------------------------------------------------------------------------------/

My personal take, since it's as simple as print a random variable i will make it to simulate 
muultiple dices for d&d, those are D4, D6, D8, D10, D12, D20, D100, the user will choose wich one to roll

"""

import random


def rollDice(side):
    return random.randint(1, side)


dices = {"D4": 4, "D6": 6, "D8": 8, "D10": 10, "D12": 12, "D20": 20, "D100": 100}

print("D&D DICES : ")
for i in dices:
    print(i, end=" ")

sides = input("\nChoose a dice to roll as D+Sides : ").upper()

if sides in dices:
    print(rollDice(dices[sides]))
else:
    print("Invalid dice type. Please choose a valid dice.")

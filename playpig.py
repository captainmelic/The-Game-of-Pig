# Dylan Gonzalez
# Final Project
# Pig Game (1 player playable version)

import random
import os

# Clear terminal to make things cleaner
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

SCORE_TO_WIN = 100
FACES = 6  # Number of faces on the dice (standard is 6)

# intro
print("Welcome to Pig! Every turn, you can roll a dice as many times as you want, adding its value to your score for the turn.")
print("But be careful! Rolling a 1 will make you lose all of your score for that turn and move on to the next turn.")
print("To avoid this, at any point, you may choose to keep your score for the turn, adding it to your total score and moving onto the next turn.")
print("This is a one-player version, so your goal will be just to win in as few turns as possible.")
print("Alright, have fun!\n")

input("[Press Enter to start]")

commands = ["exit", "hold", "roll"]
total_score = 0
turn = 0
plyinput = ""

# main game loop
while total_score < SCORE_TO_WIN and plyinput != "exit":
    plyinput = ""
    turn += 1
    roll = 0
    turnscore = 0
    # turn loop
    while roll != 1 and plyinput != "exit" and plyinput != "hold" and turnscore + total_score < SCORE_TO_WIN:
        clear_terminal()
        print(f"Turn: {turn}")
        print(f"Your total score: {total_score}")

        roll = random.randint(1, FACES)
        if roll == 1:
            print("Oops, you rolled a one! You lose this turn's score!\n")
            turnscore = 0
        elif turnscore + roll + total_score >= SCORE_TO_WIN:
            turnscore += roll
            print(f"You rolled a {roll}! That makes your total score {total_score+turnscore}!")
        else:
            turnscore += roll
            print(f"You rolled a {roll}!\nYour current score: {turnscore}.\n")
            plyinput = input("Would you like to \"hold\" your score, or \"roll\" again? (type \"exit\" to exit)\n")

            while plyinput not in commands:
                print("Wrong input (type commands exactly as shown in \"\"s)")
                plyinput = input("Would you like to \"hold\" your score, or \"roll\" again? (type \"exit\" to exit)\n")
    
    total_score += turnscore
    if turnscore > 0 and plyinput != "exit":
        print(f"That makes your total score {total_score}!\n")
    if total_score < SCORE_TO_WIN and plyinput != "exit":
        input("Onto the next turn! [Press Enter to continue]")

# win condition
if total_score >= SCORE_TO_WIN:
    print(f"You win! It took you {turn} turn(s).")
    
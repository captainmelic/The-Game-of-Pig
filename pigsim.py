# Dylan Gonzalez
# Final Project
# Pig Simulator for 1 player playable version

import random
import os

# Clear terminal to make things cleaner
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

SCORE_TO_WIN = 100
FACES = 6  # Number of faces on the dice (standard is 6)




k = int(input("Enter what number the computer should hold at:\n"))
n = int(input("How many times should the simulator run?\n"))
average = 0
minimum = 2147483647
maximum = 0
print("Running...")
for i in range(n):
    plyinput = ""
    total_score = 0
    turn = 0
    # main game loop
    while total_score < SCORE_TO_WIN:
        plyinput = ""
        turn += 1
        roll = 0
        turnscore = 0
        # turn loop
        while roll != 1 and plyinput != "hold" and turnscore + total_score < SCORE_TO_WIN:
            roll = random.randint(1, FACES)
            if roll == 1:
                turnscore = 0
            else:
                turnscore += roll

                #handle input here
                if(turnscore >= k):
                    plyinput = "hold"
                else:
                    plyinput = "roll"
        
        total_score += turnscore
    print(f"Won in {turn} turns!")

    # statistics
    if(turn < minimum):
        minimum = turn
    if(turn > maximum):
        maximum = turn
    average += turn

average /= n

print(f"Done! Finished on average in {average} turns, with a minimum of {minimum} turns and maximum of {maximum} turns.")


    
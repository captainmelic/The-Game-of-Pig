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




mink = int(input("Enter the minimum number the computer should hold at:\n"))
maxk = int(input("Enter the maximum number the computer should hold at:\n"))
n = int(input("How many times should each simulator run?\n"))

minavg = 2147483647
minavgk = 0

print("Running...")
for k in range(mink,maxk+1):
    average = 0
    minimum = 2147483647
    maximum = 0
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

        # statistics
        if(turn < minimum):
            minimum = turn
        if(turn > maximum):
            maximum = turn
        average += turn

    average /= n

    if(average < minavg):
        minavg = average
        minavgk = k

    print(f"Done! While Holding at {k} Finished on average in {average} turns, with a minimum of {minimum} turns and maximum of {maximum} turns.")

print(f"\nThe k with the lowest average is {minavgk} with an average of winning in {minavg} turns.")


    
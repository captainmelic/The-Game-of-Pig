# Dylan Gonzalez
# Final Project
# Pig Simulator for 1 player playable version

import random
import matplotlib.pyplot as plt
import numpy as np


SCORE_TO_WIN = 100
FACES = 6  # Number of faces on the dice (standard is 6)




mink = int(input("Enter the minimum number the computer should hold at:\n"))
maxk = int(input("Enter the maximum number the computer should hold at:\n"))
n = int(input("How many times should each simulator run?\n"))

k_values = list(range(mink, maxk + 1))
averages = []  # To store average turns for each k
minavg = float('inf')  # Initialize to a very large value
minavgk = 0

print("Running...")
for k in range(mink,maxk+1):
    average = 0
    minimum = float('inf')
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
        minimum = min(minimum, turn)
        maximum = max(maximum, turn)
        average += turn

    average /= n
    averages.append(average)

    if(average < minavg):
        minavg = average
        minavgk = k

    print(f"Done! While Holding at {k} Finished on average in {average:.2f} turns, with a minimum of {minimum} turns and maximum of {maximum} turns.")

print(f"\nThe k with the lowest average is {minavgk:.2f} with an average of winning in {minavg:.2f} turns.")

plt.figure(figsize=(10, 6))
plt.plot(k_values, averages, marker='o', label="Average Turns")
plt.axvline(minavgk, color='r', linestyle='--', label=f"Optimal k = {minavgk}")
plt.title("Average Turns to Win vs. Hold Threshold (k)")
plt.xlabel("Hold Threshold (k)")
plt.ylabel("Average Turns to Win")
plt.grid(True)
plt.legend()
plt.xticks(ticks=k_values)
plt.show()
    
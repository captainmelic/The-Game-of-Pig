# Dylan Gonzalez
# Final Project
# Pig Simulator for 1 player playable version, this time giving probabilities of winning in a certain number of turns while holding at a certain number

import random

SCORE_TO_WIN = 100
FACES = 6  # Number of faces on the dice (standard is 6)


k = int(input("Enter what number the computer should hold at:\n"))
t = int(input("Enter how many turns they have to win by:\n"))
n = int(input("How many times should the simulator run?\n"))
times_won = 0
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

    if(turn <= t):
        times_won += 1

print(f"Done! Won in {t} turns {times_won} times out of {n} games , a probability of {times_won/n}.")


    
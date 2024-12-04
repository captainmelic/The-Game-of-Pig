# Dylan Gonzalez
# Final Project
# Pig Game (1 player vs. opponent holding at 20 version)

import random
import os

# Clear terminal to make things cleaner
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

SCORE_TO_WIN = 100
FACES = 6  # Number of faces on the dice (standard is 6)

# Intro
print("Welcome to Pig! Every turn, you can roll a dice as many times as you want, adding its value to your score for the turn.")
print("But be careful! Rolling a 1 will make you lose all of your score for that turn and move on to the next turn.")
print("To avoid this, at any point, you may choose to keep your score for the turn, adding it to your total score and moving onto the next turn.")
print("Now, you'll be playing against an opponent who always holds at a score of 20 each turn.")
print("The first player to reach 100 points wins. Good luck!\n")

input("[Press Enter to start]")

commands = ["exit", "hold", "roll"]
player_score = 0
opponent_score = 0
turn = 0

# Main game loop
while player_score < SCORE_TO_WIN and opponent_score < SCORE_TO_WIN:
    turn += 1
    clear_terminal()
    print(f"Turn {turn}:")
    print(f"Your total score: {player_score}")
    print(f"Opponent's total score: {opponent_score}\n")
    
    # Player's turn
    print("Your turn!")
    player_turnscore = 0
    player_roll = 0
    player_input = ""
    while player_roll != 1 and player_input != "exit" and player_input != "hold" and player_turnscore + player_score < SCORE_TO_WIN:
        player_roll = random.randint(1, FACES)
        if player_roll == 1:
            print("Oops, you rolled a one! You lose this turn's score!\n")
            player_turnscore = 0
        else:
            player_turnscore += player_roll
            print(f"You rolled a {player_roll}!")
            print(f"Your current turn score: {player_turnscore}.\n")
            if player_turnscore + player_score >= SCORE_TO_WIN:
                break
            player_input = input("Would you like to \"hold\" your score, or \"roll\" again? (type \"exit\" to exit)\n")
            while player_input not in commands:
                print("Invalid input. Please type \"hold\", \"roll\", or \"exit\".")
                player_input = input("Would you like to \"hold\" your score, or \"roll\" again? (type \"exit\" to exit)\n")

    player_score += player_turnscore
    if player_input == "exit":
        break
    if player_score >= SCORE_TO_WIN:
        break
    print(f"Your total score is now: {player_score}.\n")

    # Opponent's turn
    print("Opponent's turn!")
    opponent_turnscore = 0
    opponent_roll = 0
    while opponent_turnscore < 20 and opponent_roll != 1 and opponent_turnscore + opponent_score < SCORE_TO_WIN:
        opponent_roll = random.randint(1, FACES)
        if opponent_roll == 1:
            print("Opponent rolled a one! They lose this turn's score!\n")
            opponent_turnscore = 0
        else:
            opponent_turnscore += opponent_roll
            print(f"Opponent rolled a {opponent_roll}. Their current turn score: {opponent_turnscore}.\n")

    opponent_score += opponent_turnscore
    print(f"Opponent's total score is now: {opponent_score}.\n")
    input("[Press Enter to proceed to the next turn]")

# Win condition
if player_score >= SCORE_TO_WIN:
    print(f"Congratulations! You win! It took you {turn} turn(s).")
elif opponent_score >= SCORE_TO_WIN:
    print(f"Your opponent wins! Better luck next time!")
else:
    print("Game exited. Thanks for playing!")

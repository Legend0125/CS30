#######################################################
# JANREI
# Computer Science 30
# sept. 6, 2024
#
# RPS
# Purpose: play rock-paper-scissors game
# rock paper scissors
# Create a program that has you play rock paper scissors against a bot.
# ask the user for Rock, Paper, or Scissors
# compare that input against a random number between 1 and 3
# show results
# do best of 3
# ask to play again
# can't use AI
# can't break program (sanitized)
#######################################################

import random

ROCK = 1
PAPER = 2
SCISSORS = 3

user_score = 0
bot_score = 0
win_score = 3

def get_user_choice(): # user enters rock paper or scissors
    while True:
        try:
            user_choice = int(input('Choose rock (1), paper (2), or scissors (3): '))
            if user_choice not in [ROCK, PAPER, SCISSORS]:
                raise ValueError
            return user_choice
        except ValueError:
            print("Invalid choice. Please enter 1 for rock, 2 for paper, or 3 for scissors.")

def get_bot_choice(): # bot randomly chooses rock paper or scissorsdef get_bot_choice(): # bot randomly chooses rock paper or scissors
    return random.randint(ROCK, SCISSORS)

def determine_winner(user_choice, bot_choice): # compare user and bot choices and determine winner
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (user_choice == ROCK and bot_choice == SCISSORS) or \
         (user_choice == PAPER and bot_choice == ROCK) or \
         (user_choice == SCISSORS and bot_choice == PAPER): # all cases where user wins
        return "You win!"
    else: # user loses
        return "You lose!"
    return random.randint(ROCK, SCISSORS)

def play_game(): # playing the actual game
    global user_score, bot_score
    while user_score < win_score and bot_score < win_score:
        bot_choice = get_bot_choice()
        user_choice = get_user_choice()
        result = determine_winner(user_choice, bot_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            bot_score += 1
        print(f"Score: You - {user_score}, Bot - {bot_score}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    print("Game over!")
    print(f"Final score: You - {user_score}, Bot - {bot_score}") # prints the final score

play_game()
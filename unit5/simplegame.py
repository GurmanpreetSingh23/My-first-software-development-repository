"""
Project: Rock, Paper, Scissors Game
Author: [Gurmanpreet Singh]
A simple command-line game demonstrating the use of Python 
standard libraries (random, time) and extensive code commenting.
"""

# IMPORTING STANDARD LIBRARIES
# I have used 'random' to let the computer make unpredictable choices.
import random 
# I use 'time' to create delays, making the game feel more realistic.
import time   

def get_computer_choice():
    """
    Selects a random choice for the computer.
    Returns: A string ('rock', 'paper', or 'scissors').
    """
    choices = ["rock", "paper", "scissors"]
    # random.choice is a method from the standard library that picks one item from a list
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Compares the user's choice against the computer's choice to find the winner.
    
    Parameters:
    user_choice (str): The player's input.
    computer_choice (str): The computer's random selection.
    
    Returns:
    str: A message indicating if the user won, lost, or tied.
    """
    # 1. Check for a tie first as it is the simplest condition
    if user_choice == computer_choice:
        return "It's a tie!"

    # 2. Check all winning conditions for the user
    # I use a tuple of winning combinations to keep the code clean
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        return "You Win! :)"

    # 3. If it's not a tie and the user didn't win, the computer wins
    return "You Lose! :("

def play_game():
    """
    The main function to run the game loop.
    It handles user input, validation, and calling other functions.
    """
    print("Welcome to Rock, Paper, Scissors!")
    print("---------------------------------")

    while True:
        # Get input and convert to lowercase so 'Rock' and 'rock' both work
        user_input = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()

        # Check if the user wants to stop the game
        if user_input == 'quit':
            print("Thanks for playing! Goodbye.")
            break # Exits the while loop

        # Input Validation: Ensure the user typed a valid option
        valid_options = ["rock", "paper", "scissors"]
        if user_input not in valid_options:
            print("Invalid input. Please check your spelling and try again.")
            continue # Skips the rest of the loop and starts over

        # Computer makes its move
        print("Computer is thinking...")
        time.sleep(1) # Pauses the program for 1 second (functionality optimization)
        
        computer_input = get_computer_choice()
        print(f"Computer chose: {computer_input}")

        # Determine and print the result
        result = determine_winner(user_input, computer_input)
        print(result)

if __name__ == "__main__":
    play_game()
"""
Guess the number game

"""


import random

def guess_the_number():
   
    # 1. Setup the game variables
    secret_number = random.randint(1, 10) 
   # We can increase the number upto desire and also increase or decrease max attempts 
    max_attempts = 3 
    attempts_taken = 0
    
    print("--- GUESS THE NUMBER ---")
    print("I am thinking of a number between 1 and 10.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    # 2. Start the Loop Structure
    # This loop runs as long as the player has attempts left
    while attempts_taken < max_attempts:
        try:
            # Get user input
            guess = int(input(f"Attempt {attempts_taken + 1}: Enter your guess: "))
            
            # Increment the counter
            attempts_taken += 1

            # 3. Check Conditions
            if guess == secret_number:
                print(f" Correct! You guessed it in {attempts_taken} attempts.")
                break # Exit the loop immediately if they win
            
            elif guess < secret_number:
                print("Too low!")
            
            else: 
                print("Too high!")
            
            # 4. Check if they have run out of tries
            if attempts_taken == max_attempts:
                print(f"\n Game Over! Better luck next time.")
                print(f"The number was: {secret_number}")

        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
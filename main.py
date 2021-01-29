"""
This is a number guessing game, a random number between 1 and 100 is selected by the computer.
The user will have to guess the number by choosing a level that will determine how many attempts
they have to guess it right.
"""
# Imports
import random
from logo import logo

# constants
EASY = 7
HARD = 4


# Determine the user attempts
def level():
    """
    This function is used to prompt user for their desired game level.
    """
    choose = input('\nChoose a level, "easy" or "hard": ').lower()
    if choose == "hard":
        return HARD
    elif choose == "easy":
        return EASY
    else:
        print('Invalid response.')


# Validate the guess
def check_guess(rand_num, guess_num, chances):
    """
    This function checks if guessed number is the same as the random number.
    """
    if guess_num > rand_num:
        print('The guess is too high.')
        return chances - 1
    elif guess_num < rand_num:
        print('The guess is too low.')
        return chances - 1
    else:
        print(f'Correct guess, the random number was {rand_num}. Well done')


# Game application
def start_game():
    """
    This function is start the game functionality.
    """
    # Default displays
    print(logo)
    print('IMPORTANT:\n A number between 1 and 100 is chosen at random. '
          '\n Select a level (Easy or Hard).'
          '\n Easy means 7 attempts.'
          '\n Hard means 4 attempts.\n')

    # Random number chosen
    random_number = random.randint(1, 100)

    # Calling the level function
    attempts = level()

    # Add continuous iteration until declared otherwise
    game_over = False
    while not game_over:
        if attempts == 1:
            print(f"You have {attempts} attempt to guess the number.")
        else:
            print(f"You have {attempts} attempts to guess the number.")

        # User guessing
        guess = int(input('\nGuess a number: '))

        # Check that the user guess is within the constraints
        if guess < 1 or guess > 100:
            print('Your guess must be between 1 and 100.')
        else:
            attempts = check_guess(random_number, guess, attempts)

            # Prevent the game from running when
            if attempts is None:
                game_over = True
            elif attempts == 0:
                print(f"You've run out of attempts, you lose.\nThe random number was {random_number}.")
                game_over = True
            else:
                print("Guess again.")


start_game()

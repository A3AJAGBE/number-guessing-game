"""
This is a number guessing game, a random number between 1 and 100 is selected by the computer.
The user will have to guess the number by choosing a level that will determine how many attempts
they have to guess it right.
"""
# Imports
import random

# Default displays
print('IMPORTANT:\n A number between 1 and 100 is chosen at random. '
      '\n Select a level (Easy or Hard).'
      '\n Easy means 7 attempts.'
      '\n Hard means 4 attempts.\n')

# Random number chosen
random_number = random.randint(1, 100)
print(random_number)

# Add continuous iteration until declared otherwise
game_over = False
while not game_over:
    # User guessing
    guess = int(input('\nGuess a number: '))

    if guess < 1 or guess > 100:
        print('Your guess must be between 1 and 100.')
    else:
        if random_number == guess:
            print('The guess is correct. Well done')
            game_over = True
        elif random_number < guess:
            print('The guess is too high. Try again!!!')
        else:
            print('The guess is too low. Try again!!!')

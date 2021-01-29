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

# User guessing
guess = int(input('Guess a number: \n'))

if guess < 1 or guess > 100:
    print('Your guess must be between 1 and 100.')
else:
    if guess == random_number:
        print('Correct')
    else:
        print('Wrong')

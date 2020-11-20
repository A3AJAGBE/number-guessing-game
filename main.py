from logo import logo
import random

EASY = 10
HARD = 5

def level():
  """
  This function is used to set the game level.
  """
  choose = input('Choose a level, "easy" or "hard": ').lower()
  if choose == "hard":
    return HARD
  else:
    return EASY

def check_guess(random_number, guess, attempts):
  """
  This function is used verify if guessed number is the same as the random number.
  """
  if guess > random_number:
    print("Too high, Try Again.")
    return attempts - 1
  elif guess < random_number:
    print("Too low, Try Again.")
    return attempts - 1
  else:
    print("Right guess, you win.")

def start_game():
  """
  This function is start the game functionality.
  """
  print(logo)
  print("Guess a number between 1 and 100")
  random_number = random.randint(1, 101)

  attempts = level()
  guess = 0

  while guess != random_number:
    print(f"You have {attempts} attempts to guess the number.")

    guess = int(input("Your guess: "))
  
    attempts = check_guess(random_number, guess, attempts)

    if attempts == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != random_number:
      print("Guess again.")

start_game()

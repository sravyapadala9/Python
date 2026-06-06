# Project 2 - Number Guessing Game

secret_number = 7

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess. The correct number was", secret_number)
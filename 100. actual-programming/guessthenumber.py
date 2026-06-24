import random

# The computer picks a random number from 1 to 10
secret_number = random.randint(1, 10)

print("Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 10.")

guess = 0

# Keep asking until the player guesses correctly
while guess != secret_number:

    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("You guessed it!")

# Joshua Sew-Hee
# 6/15/18
# Guessing Game One

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right.
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken,
# and when the game ends, print this out.

from random import randint as generate_random_num

print("This game consists of guessing a number between 1 and 9 inclusive.")
number = generate_random_num(1,9)
# print(number)
guess = input("Your guess: ")
score = 1

while (guess != "exit"):
    if int(guess) == number:
        if score == 1:
            print("You guessed exactly right after 1 try.")
        else:
            print("You guessed exactly right after %d tries." %score)
        print("Another number was generated.")
        # reset score to 0
        score = 1
        # generate another number
        number = generate_random_num(1,9)
        # print(number)
    elif int(guess) < number:
        print("You guessed too low.")
        score = score + 1

    elif int(guess) > number:
        print("You guessed too high.")
        score = score + 1

    guess = input("Your guess: ")

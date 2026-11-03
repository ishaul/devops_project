import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        raw = input("Guess a number between 1 and {}: ".format(difficulty)).strip()
        try:
            guess = int(raw)
        except ValueError:
            print("Invalid input '{}': please enter a whole number.".format(raw))
            continue
        if 1 <= guess <= difficulty:
            return guess
        print("{} is out of range: please enter a number between 1 and {}.".format(guess, difficulty))


def compare_results(secret_number, guess):
    return secret_number == guess


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    won = compare_results(secret_number, guess)
    print("The secret number was {}.".format(secret_number))
    return won

import os
import random
import time

DISPLAY_SECONDS = 0.7
MIN_NUMBER = 1
MAX_NUMBER = 101


def generate_sequence(difficulty):
    return [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(difficulty)]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_sequence(sequence):
    print("Remember this sequence: {}".format(" ".join(str(n) for n in sequence)), flush=True)
    time.sleep(DISPLAY_SECONDS)
    clear_screen()


def get_list_from_user(difficulty):
    prompt = ("Enter the {} number(s) you saw, in the same order, separated by spaces "
              "(each from {} to {}): ".format(difficulty, MIN_NUMBER, MAX_NUMBER))
    while True:
        parts = input(prompt).split()
        if len(parts) != difficulty:
            print("Expected exactly {} number(s) but got {}. Try again.".format(difficulty, len(parts)))
            continue
        try:
            numbers = [int(part) for part in parts]
        except ValueError:
            print("All values must be whole numbers. Try again.")
            continue
        if all(MIN_NUMBER <= n <= MAX_NUMBER for n in numbers):
            return numbers
        print("All numbers must be between {} and {}. Try again.".format(MIN_NUMBER, MAX_NUMBER))


def is_list_equal(list_a, list_b):
    return list_a == list_b


def play(difficulty):
    sequence = generate_sequence(difficulty)
    show_sequence(sequence)
    answer = get_list_from_user(difficulty)
    won = is_list_equal(sequence, answer)
    print("The sequence was: {}".format(" ".join(str(n) for n in sequence)))
    return won

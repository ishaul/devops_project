import CurrencyRouletteGame
import GuessGame
import MemoryGame

GAMES = {
    1: ("Memory Game",
        "a sequence of numbers will appear for 0.7 seconds and you have to guess it back",
        MemoryGame),
    2: ("Guess Game",
        "guess a number and see if you chose like the computer",
        GuessGame),
    3: ("Currency Roulette",
        "try and guess the value of a random amount of USD in ILS",
        CurrencyRouletteGame),
}

MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 5


def welcome(name):
    return ("Hello {} and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.".format(name))


def get_int_in_range(prompt, low, high):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Invalid input '{}': please enter a whole number from {} to {}.".format(raw, low, high))
            continue
        if low <= value <= high:
            return value
        print("{} is out of range: please enter a whole number from {} to {}.".format(value, low, high))


def load_game():
    print("Please choose a game to play:")
    for number, (title, description, _) in GAMES.items():
        print("{}. {} - {}".format(number, title, description))
    game_choice = get_int_in_range("Your choice: ", 1, len(GAMES))

    difficulty = get_int_in_range(
        "Please choose game difficulty from {} to {}: ".format(MIN_DIFFICULTY, MAX_DIFFICULTY),
        MIN_DIFFICULTY, MAX_DIFFICULTY)

    title, _, game = GAMES[game_choice]
    print("\nStarting {} at difficulty {}...\n".format(title, difficulty))
    try:
        won = game.play(difficulty)
    except CurrencyRouletteGame.RoundCancelledError as error:
        print("Round cancelled: {}. No result was recorded.".format(error))
        return None

    print("You won! Well done." if won else "You lost. Better luck next time.")
    return won

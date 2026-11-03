import random
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

import requests

API_URL = "https://api.frankfurter.dev/v1/latest"
REQUEST_TIMEOUT_SECONDS = 5
MAX_DIFFICULTY = 5
CENTS = Decimal("0.01")


class RoundCancelledError(Exception):
    pass


def generate_amount():
    return random.randint(1, 100)


def get_exchange_rate():
    try:
        response = requests.get(API_URL, params={"base": "USD", "symbols": "ILS"},
                                timeout=REQUEST_TIMEOUT_SECONDS)
        response.raise_for_status()
        rate = Decimal(str(response.json()["rates"]["ILS"]))
    except (ValueError, KeyError, TypeError, InvalidOperation):
        raise RoundCancelledError("the currency API returned an invalid or incomplete response")
    except requests.RequestException as error:
        raise RoundCancelledError("could not reach the currency API ({})".format(error))
    if not rate.is_finite() or rate <= 0:
        raise RoundCancelledError("the currency API returned an invalid USD/ILS rate")
    return rate


def to_money(value):
    return Decimal(value).quantize(CENTS, rounding=ROUND_HALF_UP)


def get_money_interval(difficulty, amount, rate):
    total = to_money(Decimal(amount) * Decimal(rate))
    margin = Decimal(MAX_DIFFICULTY - difficulty)
    return total - margin, total + margin


def get_guess_from_user(amount):
    while True:
        raw = input("How many ILS is {} USD worth? ".format(amount)).strip()
        try:
            guess = Decimal(raw)
        except InvalidOperation:
            print("Invalid input '{}': please enter a number such as 42 or 42.50.".format(raw))
            continue
        if guess.is_finite() and guess >= 0:
            return to_money(guess)
        print("Please enter a valid non-negative number.")


def play(difficulty):
    amount = generate_amount()
    rate = get_exchange_rate()
    lower, upper = get_money_interval(difficulty, amount, rate)
    guess = get_guess_from_user(amount)
    print("{} USD is {} ILS (rate {}). Accepted range: {} to {}.".format(
        amount, to_money(amount * rate), rate, lower, upper))
    return lower <= guess <= upper

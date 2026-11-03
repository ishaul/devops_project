from Live import load_game, welcome


def main():
    try:
        name = input("Please enter your name: ").strip() or "Player"
        print(welcome(name))
        load_game()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()

def play(player_number):
    pass


def main():
    running = True
    print("Roll the dice!")
    while running:
        print("Please enter a number:")
        command = input()
        if command == 'quit':
            running = False
            print("Thanks for playing!")
        else:
            play(int(command))


if __name__ == "__main__":
    main()

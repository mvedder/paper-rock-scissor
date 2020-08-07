import random


def play_computer(computer_number):
    print("\u001b[33mComputer rolled " + str(computer_number) + "\033[0m")


def computer_role():
    n = random.randint(1, 6)
    return n


def computer_announcement(computer_number, player_number):  # f(x,y)
    if player_number > computer_number:
        print("\u001b[32;1mYou won \033[0m")
    elif player_number == computer_number:
        print ("\u001b[37;1mDraw \033[0m")
    else:
        print("\u001b[31mYou lost \033[0m")


def play(player_number):
    print("\033[94mYou rolled " + str(player_number) + "\033[0m")
    computer_number = computer_role()
    play_computer(computer_number)
    computer_announcement(computer_number, player_number)
    # print("You lost!") oder print("You won!") je nachdem wer gewonnen hat


def main():
    running = True
    print("Roll the dice!")
    while running:
        print("Please write role:")
        command = input()
        if command == 'quit':
            running = False
            print("Thanks for playing!")
        else:
            play(random.randint(1, 6))


if __name__ == "__main__":
    main()

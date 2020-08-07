# Best of three
def check_valid_command(command):  # command = paper
    if command.lower() not in ["scissor", "paper", "rock"]:
        return False
    else:
        return True


def check_winner_command(player1, player2):  # player1 = scissor, player2 = rock
    if player1.lower() == "scissor" and player2.lower() == "rock":
        return player2
    elif player1.lower() == "scissor" and player2.lower() == "paper":
        return player1
    elif player1.lower() == "rock" and player2.lower() == "paper":
        return player2

def main():
    running = True
    print("Welcome")
    while running:
        print("[Player 1] Please choose one of the following options: Rock, Paper or Scissor")
        command = input()
        if command == 'quit':
            running = False
            print("Thanks for playing!")
        else:
            pass
    # Ist die eingabe korrekt
    # Speichere eingabe für player1 und player 2
    # wurde 2 mal was eingegeben?
    # checke wer gewonnen hat?


if __name__ == "__main__":
    main()

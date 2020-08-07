from getpass import getpass


def check_valid_command(command):
    if command.lower() not in ["scissor", "paper", "rock"]:
        return False
    else:
        return True


def check_winner_command(player1, player2):
    if player1.lower() == "scissor" and player2.lower() == "rock":
        return "Player 2"
    elif player1.lower() == "scissor" and player2.lower() == "paper":
        return "Player 1"
    elif player1.lower() == "rock" and player2.lower() == "paper":
        return "Player 2"
    elif player1.lower() == "rock" and player2.lower() == "scissor":
        return "Player 1"
    elif player1.lower() == "paper" and player2.lower() == "rock":
        return "Player 1"
    elif player1.lower() == "paper" and player2.lower() == "scissor":
        return "Player 2"
    else:
        return None


def main():
    running = True
    print("Welcome")
    print("[Player 1] Please choose one of the following options: Rock, Paper or Scissor")
    player1 = None
    player2 = None
    while running:
        command = getpass("selection ")
        if command == 'quit':
            running = False
            print("Thanks for playing!")
        else:
            if player1 is None and player2 is None:
                if check_valid_command(command):
                    player1 = command
                    print("[Player 1] chose successfully")
                    print("[Player 2] Please choose one of the following options: Rock, Paper or Scissor")
                else:
                    print ("Please retry and choose one of the following options: rock,paper or scissor")
            elif player1 != None and player2 is None:
                if check_valid_command(command):
                    player2 = command
                    print("[Player 2] chose successfully")
                else:
                    print ("Please retry and choose one of the following options: rock,paper or scissor")
                winner = check_winner_command(player1, player2)
                print("Player 1 selection: " + player1)
                print("Player 2 selection: " + player2)
                if winner is None:
                    print ("Draw")
                else:
                    print("You won, " + winner + "!")
                running = False


if __name__ == "__main__":
    main()

from prs import check_valid_command, check_winner_command


def test_should_check_paper_valid_command():
    assert check_valid_command("paper") is True


def test_should_check_paper_capital_p_valid_command():
    assert check_valid_command("PAPER") is True


def test_should_check_rock_valid_command():
    assert check_valid_command("rock") is True


def test_should_check_scissor_valid_command():
    assert check_valid_command("scissor") is True


def test_should_check_false_command():
    assert check_valid_command("kacka") is False


def test_should_check_player_1_won():
    player1 = "scissor"
    player2 = "paper"
    assert "Player 1" == check_winner_command(player1, player2)


def test_should_check_player_2_won():
    player1 = "scissor"
    player2 = "rock"
    assert "Player 2" == check_winner_command(player1, player2)


def test_should_check_player_2_won_capitol_R():
    player1 = "scissor"
    player2 = "Rock"
    assert "Player 2" == check_winner_command(player1, player2)


def test_should_check_player2_rock_paper():
    player1 = "rock"
    player2 = "paper"
    assert "Player 2" == check_winner_command(player1, player2)


def test_should_check_player1_rock_scissor():
    player1 = "rock"
    player2 = "scissor"
    assert "Player 1" == check_winner_command(player1, player2)


def test_should_check_player1_paper_rock():
    player1 = "paper"
    player2 = "rock"
    assert "Player 1" == check_winner_command(player1, player2)


def test_should_check_player1_paper_scissor():
    player1 = "paper"
    player2 = "scissor"
    assert "Player 2" == check_winner_command(player1, player2)


def test_should_check_draw_scissor():
    player1 = "scissor"
    player2 = "scissor"
    assert None == check_winner_command(player1, player2)


def test_should_check_draw_rock():
    player1 = "rock"
    player2 = "rock"
    assert None == check_winner_command(player1, player2)


def test_should_check_draw_paper():
    player1 = "paper"
    player2 = "paper"
    assert None == check_winner_command(player1, player2)

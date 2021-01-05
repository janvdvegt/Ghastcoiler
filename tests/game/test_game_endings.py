from ghastcoiler.minions.rank_1 import PunchingBag, FiendishServant, DragonspawnLieutenant


def test_simple_ending(initialized_game):
    # One player has minions and the other does not
    player0board = initialized_game.player_board[0]
    player1board = initialized_game.player_board[1]

    player0board.add_minion(FiendishServant())
    player1board.add_minion(DragonspawnLieutenant())

    minion = player0board.select_attacking_minion()
    initialized_game.attack(minion, player1board.minions[0])
    initialized_game.check_deaths(player0board, player1board)

    assert(initialized_game.finished())
    assert(initialized_game.calculate_score_player_0() == -(player1board.rank + player1board.minions[0].rank))

def test_draw(initialized_game):
    # Make sure draws are detected. Base case is empty boards
    assert(initialized_game.finished())
    assert(initialized_game.calculate_score_player_0() == 0)

    # Test boards with only 0 power minions
    initialized_game.player_board[0].add_minion(PunchingBag())
    initialized_game.player_board[1].add_minion(PunchingBag())
    assert(initialized_game.finished())
    assert(initialized_game.calculate_score_player_0() == 0)

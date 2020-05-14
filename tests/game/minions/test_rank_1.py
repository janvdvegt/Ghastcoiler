from ghastcoiler.minions.rank_1 import FiendishServant, DragonspawnLieutenant


def test_fiendish_servant_deathrattle(initialized_game):
    initialized_game.player_board[0].add_minion(FiendishServant(), position=0)
    initialized_game.player_board[0].add_minion(DragonspawnLieutenant(), position=1)
    initialized_game.player_board[1].add_minion(FiendishServant(), position=0)
    initialized_game.attack(initialized_game.player_board[0].minions[0], initialized_game.player_board[1].minions[0])
    initialized_game.check_deaths(initialized_game.player_board[0], initialized_game.player_board[1])
    assert len(initialized_game.player_board[0].minions) == 1
    assert len(initialized_game.player_board[1].minions) == 0
    assert initialized_game.player_board[0].minions[0].attack == 4
from ghastcoiler.minions.rank_1 import FiendishServant, DragonspawnLieutenant, RabidSaurolisk


def test_fiendish_servant_deathrattle(initialized_game):
    initialized_game.player_board[0].add_minion(FiendishServant())
    initialized_game.player_board[0].add_minion(DragonspawnLieutenant())
    initialized_game.player_board[1].add_minion(FiendishServant())
    initialized_game.attack(initialized_game.player_board[0].minions[0], initialized_game.player_board[1].minions[0])
    initialized_game.check_deaths(initialized_game.player_board[0], initialized_game.player_board[1])
    assert len(initialized_game.player_board[0].minions) == 1
    assert len(initialized_game.player_board[1].minions) == 0
    assert initialized_game.player_board[0].minions[0].attack == 4


def test_rabid_saurolisk(initialized_game):
    rabid_saurolisk = RabidSaurolisk()
    initialized_game.player_board[0].add_minion(rabid_saurolisk)
    assert rabid_saurolisk.attack == 3
    assert rabid_saurolisk.defense == 1
    initialized_game.player_board[0].add_minion(FiendishServant())
    assert rabid_saurolisk.attack == 4
    assert rabid_saurolisk.defense == 2
    initialized_game.player_board[0].add_minion(DragonspawnLieutenant())
    assert rabid_saurolisk.attack == 4
    assert rabid_saurolisk.defense == 2

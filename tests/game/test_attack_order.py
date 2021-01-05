from ghastcoiler.minions.rank_1 import FiendishServant, DragonspawnLieutenant, RabidSaurolisk, PunchingBag, WrathWeaver
from ghastcoiler.minions.rank_2 import HarvestGolem, RatPack


def test_simple_attack_sequence(initialized_game):
    # Minions attack from left to right, rolling over and starting over again
    initialized_game.player_turn = 0
    player0board = initialized_game.player_board[0]
    player1board = initialized_game.player_board[1]

    # Create arbitrary board
    player0board.add_minion(FiendishServant())
    player0board.add_minion(DragonspawnLieutenant())
    player0board.add_minion(WrathWeaver())

    player1board.add_minion(PunchingBag())

    # Test 0 power board
    minion = player1board.select_attacking_minion()
    assert(minion is None)

    # Run through basic attack order twice
    for _ in range (2):
        for i in range(len(player0board.minions)):
            minion = player0board.select_attacking_minion()
            assert(minion.name == player0board.minions[i].name)
            initialized_game.attack(minion, player1board.minions[0])
            minion.attacked = True

    # 0 power minions should be skipped
    player1board.add_minion(WrathWeaver())
    assert(player1board.select_attacking_minion().name == "Wrath Weaver")


def test_simple_defender_selection(initialized_game):
    # TODO: Make sure taunts are selected over non-taunts, test other specific taunt override mechanics
    assert(True)

def test_minion_insertion(initialized_game):
    # Test that a newly inserted minion attacks in order correctly
    player0board = initialized_game.player_board[0]
    player1board = initialized_game.player_board[1]
    player0board.add_minion(HarvestGolem())
    player0board.add_minion(DragonspawnLieutenant())
    player1board.add_minion(PunchingBag())
    player1board.minions[0].attack = 999

    minion = player0board.select_attacking_minion()
    initialized_game.attack(minion, player1board.minions[0])
    initialized_game.check_deaths(player0board, player1board)
    minion.attacked = True

    # If a minion attacks, dies, and creates one or more minions, they should be next in the attack order
    minion = player0board.select_attacking_minion()
    assert(minion.name == "Damaged Golem")

def test_minion_insertion_multiple(initialized_game):
    # Test that a minion inserted before the attack order doesnt disrupt attack order
    player0board = initialized_game.player_board[0]
    player1board = initialized_game.player_board[1]
    
    player0board.add_minion(RatPack())
    player0board.add_minion(DragonspawnLieutenant())

    player1board.add_minion(PunchingBag())

    # Attack with Rat
    minion = player0board.select_attacking_minion()
    initialized_game.attack(minion, player1board.minions[0])
    minion.attacked = True

    # Kill The rat, creating tokens. This simulates the enemy board killing it
    initialized_game.kill(minion, player0board, player1board, False)
    assert(len(player0board.minions) == 3)
    assert(player0board.minions[0].name and player0board.minions[1].name == "Rat")

    # Next minion to attack should still be the dragon (rats are inserted before it)
    minion = player0board.select_attacking_minion()
    initialized_game.attack(minion, player1board.minions[0])
    assert(minion.name == "Dragonspawn Lieutenant")



    

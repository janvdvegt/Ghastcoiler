import logging

from utils.profile import Profile

from game.game_instance import GameInstance
from game.simulation import Simulation
from game.player_board import PlayerBoard

from minions.rank_1 import DragonspawnLieutenant, FiendishServant, DireWolfAlpha, RedWhelp, RighteousProtector, Mecharoo


player_board_0 = PlayerBoard(player_id=0, hero=None, life_total=12, rank=4, minions=[FiendishServant(), DragonspawnLieutenant(), DireWolfAlpha(), DragonspawnLieutenant(), RedWhelp(), RedWhelp()])
player_board_1 = PlayerBoard(player_id=1, hero=None, life_total=12, rank=4, minions=[DragonspawnLieutenant(), Mecharoo(), FiendishServant(), DragonspawnLieutenant(), FiendishServant(), RighteousProtector(), RighteousProtector()])

simulation = Simulation(player_board=player_board_0, opponent_board=player_board_1, max_simulations=50)

# logging.DEBUG will show all steps in combat
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

with Profile():
    print(simulation.simulate()) # List of tuples with outcome and the frequency of that outcome

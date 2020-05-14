import pytest

from ghastcoiler.game.game_instance import GameInstance
from ghastcoiler.game.player_board import PlayerBoard


@pytest.fixture
def initialized_game():
    return GameInstance(player_board_0=PlayerBoard(player_id=0, hero=None, life_total=1, rank=1, minions=[]),
                        player_board_1=PlayerBoard(player_id=1, hero=None, life_total=1, rank=1, minions=[]))

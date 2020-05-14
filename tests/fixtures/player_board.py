import pytest

from ghastcoiler.game.player_board import PlayerBoard


@pytest.fixture
def empty_board():
    return PlayerBoard(player_id=0, hero=None, life_total=1, rank=1, minions=[])

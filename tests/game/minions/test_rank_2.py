from ghastcoiler.minions.rank_2 import GlyphGuardian, HarvestGolem, Imprisoner, KaboomBot, KindlyGrandmother


def test_kaboombot_deathrattle(initialized_game):
    kaboom_bot = KaboomBot()
    glyph_guardian = GlyphGuardian()
    initialized_game.player_board[0].add_minion(kaboom_bot)
    initialized_game.player_board[1].add_minion(glyph_guardian)
    initialized_game.attack(kaboom_bot, glyph_guardian)
    assert glyph_guardian.defense == 2
    initialized_game.check_deaths(initialized_game.player_board[0], initialized_game.player_board[1])
    assert glyph_guardian.defense == -2

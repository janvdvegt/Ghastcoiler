class Deathrattle:
    def __init__(self, name):
        """Base Deathrattle class that should be inherited from by all deathrattle triggers

        Arguments:
            name {string} -- [name of the Deathrattle, when of specific minion use MinionNameDeathrattle]
        """
        self.name = name

    def trigger(self, minion, own_board, opposing_board):
        """Trigger that is called once or multiple times (with Deathbaron) when minion that has this Deathrattle dies

        Arguments:
            minion {Minion} -- Minion that died with this Deathrattle, certain features could be important, for example the attack on the Fiendish Servant
            own_board {PlayerBoard} -- Player board of the minion that died
            opposing_board {PlayerBoard} -- Player board of the opposing player of the minion that died
        """
        pass
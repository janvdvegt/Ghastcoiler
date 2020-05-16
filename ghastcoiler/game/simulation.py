from collections import Counter

from game.game_instance import GameInstance
from game.player_board import PlayerBoard


class Simulation:
    def __init__(self, player_board: PlayerBoard, opponent_board: PlayerBoard, max_simulations: int = 10000, time_budget_in_milliseconds: int = 1000):
        """Simulation object to analyze certain scenarios

        Arguments:
            player_board {PlayerBoard} -- Player board
            opponent_board {PlayerBoard} -- Opposing player board

        Keyword Arguments:
            max_simulations {int} -- Maximum number of simulations ti run (default: {10000})
            time_budget_in_milliseconds {int} -- Maximum number of milliseconds to run simulations - CURRENTLY NOT USED YET (default: {1000})
        """
        self.player_board = player_board
        self.opponent_board = opponent_board
        self.max_simulations = max_simulations
        self.time_budget_in_milliseconds = time_budget_in_milliseconds

    def simulate(self):
        """Start simulation

        Returns:
            List[Tuple[(int, int)]] -- List of tuples with the shape of (Outcome, Frequency)
        """
        scores = []
        for simulation_index in range(self.max_simulations):
            game_instance = GameInstance(player_board_0=self.player_board.copy(), player_board_1=self.opponent_board.copy(), player_turn=simulation_index % 2)
            scores.append(game_instance.start())
        counter = Counter(scores)
        return sorted(counter.items(), key=lambda x: x[0])
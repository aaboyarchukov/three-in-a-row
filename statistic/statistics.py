from any import Any

class Statistics(Any):
    # constructor
    def __init__(self):
        self.moves = 0
        self.total_points = 0
    
    # commands

    # post-cond: points are increased
    def update_points(self):
        pass
    
    # post-cond: amount of moves are increased
    def update_moves_amount(self):
        pass

    def show_interim_results(self):
        print(self.get_interim_result())

    def show_final_results(self):
        print(self.get_final_result())

    # requests

    # post-cond: get actual points
    def get_points(self) -> int:
        pass
    
    # post-cond: get actual amount of moves
    def get_amount_moves(self) -> int:
        pass
    
    # post-cond: get pretty result
    def get_final_result(self) -> str:
        pass

    # post-cond: get intermediate result
    def get_interim_result(self) -> str:
        points = self.total_points
        moves = self.moves

        return f'current points: {points} \ncurrent moves: {moves}'
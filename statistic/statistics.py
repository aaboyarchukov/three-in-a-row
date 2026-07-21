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
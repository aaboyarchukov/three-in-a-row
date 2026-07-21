from any import Any

class Game(Any):
    # constructor
    def __init__(self):
        pass    
    
    # commands
    # pre-cond: game is not ending yet
    # post-cond: game ending
    def end_game(self):
        pass
    
    # pre-cond: 
    #   - game is not ending yet
    #   - dependecies are init
    # post-cond: game ending
    def start_game(self):
        pass

    # requests
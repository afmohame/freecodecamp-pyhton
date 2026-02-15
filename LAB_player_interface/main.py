from abc import ABC, abstractmethod
import random
class Player(ABC):
    def __init__(self):
        #x is left/right and y is up/down and x & y do diagonal movement
        self.moves = [] 
        self.position = (0,0)
        self.path = [self.position]
    
    def make_move(self):
        pos = random.choice(self.moves)
        self.position = (pos[0] + self.position[0], pos[1] + self.position[1])
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def level_up(self):
        self.moves = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (-1, 0), (0, -1)]
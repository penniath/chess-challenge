from abc import abstractmethod


class Piece:
    
    type = '_'
    
    def __eq__(self, other):
        return self.type == other.type
    
    def __hash__(self):
        return hash(self.type)
    
    def check_positions(self, board, x, y):
        for i, j in self.get_all_positions(board, x, y):
            if not self.check_position(board, i, j):
                return False

        return True
    
    @abstractmethod
    def check_position(self, board, x, y):
        try:
            val = board.get_position_value(x, y)
            return val is None or val == '-1'
        except Exception:
            return True
    
    @abstractmethod
    def mark_positions(self, board, x, y):
        for i, j in self.get_all_positions(board, x, y):
            board.set_position_value(i, j, '-1')
            
    @abstractmethod
    def get_type(self):
        return self.type
    
    @abstractmethod
    def get_all_positions(self, board, x, y): pass

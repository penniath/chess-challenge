from abc import abstractmethod


class Piece:
    
    @abstractmethod
    def check_positions(self, board, x, y): pass
    
    @abstractmethod
    def mark_positions(self, board, x, y): pass
    
    @abstractmethod
    def get_all_positions(self, board, x, y): pass
    
    @abstractmethod
    def get_type(self): pass
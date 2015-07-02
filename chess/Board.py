from copy import copy

class Board:
    
    def __init__(self, width, height, board=None):
        self.width = width
        self.height = height
        self.board = board
        
        if self.board is None:
            self.board = [None] * width * height
        
    def __copy__(self):
        return Board(self.width, self.height, copy(self.board))
    
    def __eq__(self, other):
        if self.width != other.width or self.height != other.height:
            return False
        
        x = y = 0;
        while not self.is_out_of_bounds(x, y):
            if self.get_position_value(x, y) != other.get_position_value(x, y):
                return False
            x, y = self.get_next_position(x, y)
            
        return True
    
    def __hash__(self):
        return hash(tuple(self.board))
    
    def get_position_value(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            raise Exception("Out of bounds")
        i = x + y * self.width
        return self.board[i]
        
    def set_position_value(self, x, y, value):
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            i = x + y * self.width
            self.board[i] = value
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
        
    def is_out_of_bounds(self, x, y):
        i = x + y * self.width
        last = self.width * self.height
        return i < 0 or i >= last
        
    def get_next_position(self, x, y):
        i = x + y * self.width + 1
        return (i%self.width, i//self.width)
        
    def get_board(self):
        return self.board
    
    def count_empty_positions(self):
        count = 0
        for cell in self.board:
            if cell is None:
                count+= 1
        return count
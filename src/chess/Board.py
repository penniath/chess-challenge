import itertools

class Board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [None] * width * height
    
    def get_position_value(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            raise Exeption("Out of bounds")
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
        
    def is_last_position(self, x, y):
        i = x + y * self.width
        last = self.width * self.height - 1
        return i == last
        
    def get_next_position(self, x, y):
        i = x + y * self.width + 1
        return (i%self.width, i//self.width)
        
    def get_board(self):
        return self.board
class Rook:
    
    type = 'R'
    
    def __init__(self):
        pass
    
#     @staticmethod
    def check_positions(self, board, x, y):
        for i in range(x+1, board.get_width()):
            if not self.check_position(board, i, y): return False
            
        for i in range(x-1, -1, -1):
            if not self.check_position(board, i, y): return False
            
        for j in range(y+1, board.get_height()):
            if not self.check_position(board, x, j): return False
        
        for j in range(y-1, -1, -1):  
            if not self.check_position(board, x, j): return False
        
        return True
        
        
#     @staticmethod
    def check_position(self, board, x, y):
        try:
            val = board.get_position_value(x, y)
            return val is None or val == '-1'
        except Exception:
            return True
        
    
    def mark_positions(self, board, x, y):
        for i in range(x+1, board.get_width()):
            board.set_position_value(i, y, '-1')
            
        for i in range(x-1, -1, -1):
            board.set_position_value(i, y, '-1')
            
        for j in range(y+1, board.get_height()):
            board.set_position_value(x, j, '-1')
        
        for j in range(y-1, -1, -1):  
            board.set_position_value(x, j, '-1')
            
    def get_type(self):
        return self.type
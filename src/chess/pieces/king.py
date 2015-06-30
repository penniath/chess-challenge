class King:
    
    type = 'K'
    
#     @staticmethod
    def check_positions(self, board, x, y):
        if not self.check_position(board, x-1, y-1): return False
        if not self.check_position(board, x, y-1): return False
        if not self.check_position(board, x+1, y-1): return False
        if not self.check_position(board, x-1, y): return False
        if not self.check_position(board, x+1, y): return False
        if not self.check_position(board, x-1, y+1): return False
        if not self.check_position(board, x, y+1): return False
        if not self.check_position(board, x+1, y+1): return False
        
        return True
        
        
#     @staticmethod
    def check_position(self, board, x, y):
        try:
            val = board.get_position_value(x, y)
            return val is None or val == '-1'
        except Exception:
            return True
        
    
    def mark_positions(self, board, x, y):
        board.set_position_value(x-1, y-1, '-1')
        board.set_position_value(x, y-1, '-1')
        board.set_position_value(x+1, y-1, '-1')
        board.set_position_value(x-1, y, '-1')
        board.set_position_value(x+1, y, '-1')
        board.set_position_value(x-1, y+1, '-1')
        board.set_position_value(x, y+1, '-1')
        board.set_position_value(x+1, y+1, '-1')
        
    def get_type(self):
        return self.type
        
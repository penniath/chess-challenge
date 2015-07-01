from src.chess.pieces.piece import Piece


class Rook(Piece):
    
    type = 'R'
    
    def check_positions(self, board, x, y):
        for i, j in self.get_all_positions(board, x, y):
            if not self.check_position(board, i, j): return False

        return True
        
    def check_position(self, board, x, y):
        try:
            val = board.get_position_value(x, y)
            return val is None or val == '-1'
        except Exception:
            return True
        
    
    def mark_positions(self, board, x, y):
        for i, j in self.get_all_positions(board, x, y):
            board.set_position_value(i, j, '-1')
            
    def get_type(self):
        return self.type
    
    def get_all_positions(self, board, x, y):
        positions = []
        for i in range(x+1, board.get_width()):
            positions.append((i, y))
            
        for i in range(x-1, -1, -1):
            positions.append((i, y))
            
        for j in range(y+1, board.get_height()):
            positions.append((x, j))
        
        for j in range(y-1, -1, -1):  
            positions.append((x, j))
            
        return positions
from src.chess.pieces.piece import Piece


class King(Piece):
    
    type = 'K'
    
    def check_positions(self, board, x, y):
        for i, j in self.get_all_positions(board, x, y):
            if not self.check_position(board,i, j):
                return False
        
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
        
    def get_all_positions(self, board, x, y):
        positions = []
        positions.append((x-1, y-1))
        positions.append((x, y-1))
        positions.append((x+1, y-1))
        positions.append((x-1, y))
        positions.append((x+1, y))
        positions.append((x-1, y+1))
        positions.append((x, y+1))
        positions.append((x+1, y+1))
        
        return positions
        
    def get_type(self):
        return self.type
        
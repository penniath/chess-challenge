from src.chess.pieces.piece import Piece


class Rook(Piece):
    
    type = 'R'
    
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
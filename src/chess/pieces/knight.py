from src.chess.pieces.piece import Piece

class Knight(Piece):
    
    type = 'N'
    
    def get_all_positions(self, board, x, y):
        positions = []
        positions.append((x-1, y-2))
        positions.append((x+1, y-2))
        positions.append((x-2, y-1))
        positions.append((x+2, y-1))
        positions.append((x-1, y+2))
        positions.append((x+1, y+2))
        positions.append((x-2, y+1))
        positions.append((x+2, y+1))
        
        return positions

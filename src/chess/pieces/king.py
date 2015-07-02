from src.chess.pieces.piece import Piece


class King(Piece):
    
    type = 'K'
    
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

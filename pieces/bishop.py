from pieces.piece import Piece


class Bishop(Piece):
    
    type = 'B'
    
    def get_all_positions(self, board, x, y):
        positions = []
        
        i = x + 1
        j = y + 1
        while i < board.get_width() and j < board.get_height():
            positions.append((i, j))
            i+= 1
            j+= 1
            
        i = x + 1
        j = y - 1
        while i < board.get_width() and j >= 0:
            positions.append((i, j))
            i+= 1
            j-= 1
            
        i = x - 1
        j = y + 1
        while i >= 0 and j < board.get_height():
            positions.append((i, j))
            i-= 1
            j+= 1
            
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            positions.append((i, j))
            i-= 1
            j-= 1
            
        return positions
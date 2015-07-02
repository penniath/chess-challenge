from pieces.piece import Piece


class Queen(Piece):
    
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
class ChessManager:
    
    @classmethod
    def place_pieces(cls, board, piece_list, x, y):
        if len(piece_list) == 0:
            return
            
        if board.is_last_position(x, y):
            return
        
        if board.get_position_value(x, y) != '-1':
            piece = piece_list[0]
            if piece.check_positions(board, x, y):
                board.set_position_value(x, y, piece.get_type())
                piece_list.pop(0)
                piece.mark_positions(board, x, y)
        
        x, y = board.get_next_position(x, y)
        
        cls.place_pieces(board, piece_list, x, y)
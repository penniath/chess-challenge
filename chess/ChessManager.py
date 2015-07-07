import copy


class ChessManager:
    
    @classmethod
    def place_pieces(cls, board, piece_list, x, y):
        
        board_list = set()
        if len(piece_list) == 0:
            board_list.add(board)
            return board_list
            
        if board.is_out_of_bounds(x, y):
            return board_list
        
        if board.count_empty_positions() < len(piece_list):
            return board_list
        
        board_copy =copy.copy(board)
        piece_list_copy = copy.copy(piece_list)
        if board_copy.get_position_value(x, y) != '-1':
            piece = piece_list_copy[0]
            if piece.check_positions(board_copy, x, y):
                child_boards = cls.process_free_position(
                         board_copy, piece_list_copy, x, y)
                board_list.update(child_boards)
        
        child_boards = cls.process_next_cell(board_copy, piece_list_copy, x, y)
        board_list.update(child_boards)
        
        del board_copy
        del piece_list_copy
            
        return board_list
    
    @classmethod
    def process_free_position(cls, board, piece_list, x, y):
        
        board_list = cls.process_next_cell(board, piece_list, x, y)
        
        piece = piece_list.pop(0)
        board.set_position_value(x, y, piece.get_type())
        piece.mark_positions(board, x, y)
        
        return board_list
    
    @classmethod
    def process_next_cell(cls, board, piece_list, x, y):
        i, j = board.get_next_position(x, y)
        return cls.place_pieces(board, piece_list, i, j)
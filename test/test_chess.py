import unittest

from chess.Board import Board
from chess.ChessManager import ChessManager
from pieces.king import King
from pieces.queen import Queen


class TestChess(unittest.TestCase):

    # BOARD TEST CASES
    
    def test_eq_returns_true_when_equals(self):
        board_1 = Board(3, 3)
        board_2 = Board(3, 3)
        
        self.assertTrue(board_1 == board_2)
        
    def test_eq_returns_false_when_different_dimmensions(self):
        board_1 = Board(3, 3)
        board_2 = Board(6, 6)
        
        self.assertFalse(board_1 == board_2)
        
    def test_eq_returns_false_when_cell_values_different(self):
        board_1 = Board(3, 3)
        board_2 = Board(3, 3)
        
        board_2.set_position_value(2, 2, '-1')
        
        self.assertFalse(board_1 == board_2)
        
    def test_get_position_value_returns_value_if_in_bounds(self):
        board = Board(3, 3)
        board.get_board()[0] = '-1'
        
        self.assertEqual(board.get_position_value(0, 0), '-1')
        
    def test_get_position_raises_exception_if_out_bounds(self):
        board = Board(3, 3)
        
        self.assertRaises(Exception, lambda: board.get_position_value(-1, -1))
        
    def test_set_position_value_set_properly_cell_value(self):
        board = Board(3, 3)
        board.set_position_value(1, 2, '-1')
        
        self.assertEqual(board.get_position_value(1, 2), '-1')
        
    def test_set_position_raises_exception_if_out_bounds(self):
        board = Board(3, 3)
        
        self.assertRaises(Exception, lambda: board.set_position_value(-1, -1, '-1'))
        
    def test_is_out_of_bounds_returns_false_when_in_bounds(self):
        board = Board(3, 3)
        
        self.assertFalse(board.is_out_of_bounds(2, 1))
        
    def test_is_out_of_bounds_returns_true_when_negative_positions(self):
        board = Board(3, 3)
        
        self.assertTrue(board.is_out_of_bounds(-1, 2))
        
    def test_is_out_of_bounds_returns_true_when_position_too_high(self):
        board = Board(3, 3)
        
        self.assertTrue(board.is_out_of_bounds(5, 5))
    
    def test_count_empty_positions_returns_9_for_empty_3x3_board(self):
        board = Board(3, 3)
        
        self.assertEqual(board.count_empty_positions(), 9)
        
    def test_count_empty_positions_returns_8_for_3x3_board_with_one_fullfilled(self):
        board = Board(3, 3)
        board.set_position_value(2, 2, '-1')
        
        self.assertEqual(board.count_empty_positions(), 8)
        

    # CHESS MANAGER TEST CASES
    
    def test_place_pieces_returns_board_when_no_pieces_left(self):
        board = Board(3, 3)
        board_list = ChessManager.place_pieces(board, [], 0, 0)
        
        self.assertSetEqual(board_list, set([board]))
        
    def test_place_pieces_returns_empty_when_out_of_bounds(self):
        board = Board(3, 3)
        piece_list = [King()]
        board_list = ChessManager.place_pieces(board, piece_list, -1, 2)
        
        self.assertSetEqual(board_list, set())
        
    def test_place_pieces_returns_empty_when_empty_positions_lower_than_piece_left(self):
        board = Board(3, 3)
        piece_list = [King(), King()]
        
        for i in range(0, 8):
            board.set_position_value(i%board.get_width(), i//board.get_width(), '-1')
        
        board_list = ChessManager.place_pieces(board, piece_list, 0, 0)
        
        self.assertSetEqual(board_list, set())
        
    def test_process_free_position_pops_first_piece_from_list(self):
        board = Board(3, 3)
        piece_list = [King(), Queen()]
        
        ChessManager.process_free_position(board, piece_list, 2, 2)
        
        self.assertListEqual(piece_list, [Queen()])
        
    def test_process_free_position_decrements_count_of_empty_positions(self):
        board = Board(3, 3)
        piece_list = [King()]
        count = board.count_empty_positions()
        
        ChessManager.process_free_position(board, piece_list, 2, 2)
        
        self.assertGreater(count, board.count_empty_positions())

        
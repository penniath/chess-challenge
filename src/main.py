import itertools

from src.chess.Board import Board
from src.chess.ChessManager import ChessManager
from src.chess.pieces.king import King
from src.chess.pieces.rook import Rook


def main():
    
    pieces = [King(), King(), Rook()]
    board = Board(3, 3)
    
    piece_perms = itertools.permutations(pieces)
    
    board_list = []
    for piece_perm in piece_perms:
        board_list.extend(ChessManager.place_pieces(board, list(piece_perm), 0, 0))
    
    board_set = set(board_list)
    for elem in board_set:
        print(elem.get_board())

main()
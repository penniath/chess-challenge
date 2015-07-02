import itertools

from src.chess.Board import Board
from src.chess.ChessManager import ChessManager
from src.chess.pieces.bishop import Bishop
from src.chess.pieces.king import King
from src.chess.pieces.knight import Knight
from src.chess.pieces.rook import Rook
from src.chess.pieces.queen import Queen


def main():
    
    print("Select the scenario:")
    print("\t 1: 2 Kings, 1 Rook. 3x3 Board")
    print("\t 2: 2 Rooks, 3 Knights. 4x4 Board")
    print("\t 3: 2 Kings, 2 Queens, 2 Bishops, 1 Knight. 7x7 Board")
    
    choice = int(input())
    if choice == 1:
        pieces = [King(), King(), Rook()]
        board = Board(3, 3)
    elif choice == 2:
        pieces = [Rook(), Rook(), Knight(), Knight(), Knight(), Knight()]
        board = Board(4, 4)
    elif choice == 3:
        pieces = [King(), King(), Queen(), Queen(), Bishop(), Bishop(), Knight()]
        board = Board(7, 7)
    else:
        return
    
    piece_perms = itertools.permutations(pieces)
    
    board_list = []
    for piece_perm in piece_perms:
        board_list.extend(ChessManager.place_pieces(board, list(piece_perm), 0, 0))
    
    board_set = set(board_list)
    for elem in board_set:
        print(elem.get_board())

main()
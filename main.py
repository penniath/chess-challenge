import itertools

from chess.ParameterManager import ParameterManager
from chess.ChessManager import ChessManager
from chess.BoardPrinter import BoardPrinter


def main():
    
#     print("Select the scenario:")
#     print("\t 1: 2 Kings, 1 Rook. 3x3 Board")
#     print("\t 2: 2 Rooks, 3 Knights. 4x4 Board")
#     print("\t 3: 2 Kings, 2 Queens, 2 Bishops, 1 Knight. 7x7 Board")
#     
#     choice = int(input())
#     if choice == 1:
#         pieces = [King(), King(), Rook()]
#         board = Board(3, 3)
#     elif choice == 2:
#         pieces = [Rook(), Rook(), Knight(), Knight(), Knight(), Knight()]
#         board = Board(4, 4)
#     elif choice == 3:
#         pieces = [King(), King(), Queen(), Queen(), Bishop(), Bishop(), Knight()]
#         board = Board(7, 7)
#     else:
#         return

    board, pieces = ParameterManager.get_parameters()
    
    piece_perms = set(itertools.permutations(pieces))
    
    board_list = []
    for piece_perm in piece_perms:
        board_list.extend(ChessManager.place_pieces(board, list(piece_perm), 0, 0))
    
    board_set = set(board_list)
    print()
    print("TOTAL: "+str(len(board_set)))
    for elem in board_set:
        BoardPrinter.print_board(elem)

main()
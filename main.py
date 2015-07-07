import itertools

from chess.BoardPrinter import BoardPrinter
from chess.ChessManager import ChessManager
from chess.ParameterManager import ParameterManager


def main():
    
    board, pieces = ParameterManager.get_parameters()
    
    piece_perms = set(itertools.permutations(pieces))
    
    board_list = []
    for piece_perm in piece_perms:
        board_list.extend(ChessManager.place_pieces(board, list(piece_perm), 0, 0))
    
    board_set = set(board_list)
    print('')
    print("TOTAL: "+str(len(board_set)))
    
    answer = input("Print every board configuration? (Y/n): ")
    if answer == 'Y':
        for elem in board_set:
            BoardPrinter.print_board(elem)

main()
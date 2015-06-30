from src.chess.Board import Board
from src.chess.pieces.king import King
from src.chess.pieces.rook import Rook
from src.chess.ChessManager import ChessManager


def main():
    
    pieces = [King(), King(), Rook()]
    board = Board(3, 3)
    
    ChessManager.place_pieces(board, pieces, 0, 0)
    
    print(board.get_board())

main()
from src.chess.Board import Board
from src.chess.pieces.king import King
from src.chess.pieces.queen import Queen
from src.chess.pieces.rook import Rook
from src.chess.pieces.bishop import Bishop
from src.chess.pieces.knight import Knight


class ParameterManager:
    
    @classmethod
    def get_parameters(cls):
       
        board = cls.get_dimmensions()
        pieces = cls.get_piece_list()
        
        if len(pieces) > board.get_width() * board.get_height():
            raise Exception("The number of pieces exceeds the available cell count")
        
        return (board, pieces)
        
    @classmethod
    def get_dimmensions(cls):
        
        print("Enter the dimmensions of the board.")
        width = int(input("Width:"))
        height = int(input("Height:"))
        
        board = Board(width, height)
        
        return board
    
    @classmethod
    def get_piece_list(cls):
        
        print("Set the number of each piece:")
        king_num = int(input("Kings: "))
        queen_num = int(input("Queens: "))
        rook_num = int(input("Rooks: "))
        bishop_num = int(input("Bishops: "))
        knight_num = int(input("Knights: "))
        
        piece_list = []
        piece_list.extend(cls.create_pieces(king_num, King))
        piece_list.extend(cls.create_pieces(queen_num, Queen))
        piece_list.extend(cls.create_pieces(rook_num, Rook))
        piece_list.extend(cls.create_pieces(bishop_num, Bishop))
        piece_list.extend(cls.create_pieces(knight_num, Knight))

        return piece_list
    
    @classmethod
    def create_pieces(cls, num_pieces, piece):
        pieces = []
        for i in range(0, num_pieces):
            pieces.append(piece())
        
        return pieces
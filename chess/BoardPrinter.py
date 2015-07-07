
class BoardPrinter:

    @classmethod
    def print_board(cls, board):
        cls.print_horizontal_lines(board.get_width())
        for j in range(0, board.get_height()):
            line = '| '
            for i in range(0, board.get_width()):
                val = board.get_position_value(i, j)
                if val is None or val == '-1':
                    val = ' '

                line+= val + ' | '

            print(line)
            cls.print_horizontal_lines(board.get_width())
            
        print('')


    @classmethod
    def print_horizontal_lines(cls, width):
        line = ' '
        for i in range(0, width):
            line+= '--- '

        print(line)

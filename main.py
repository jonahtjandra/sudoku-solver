from Sudoku import Sudoku
from Parser import Parser

board = Parser.parse("board.txt")
sudoku = Sudoku(board)
sudoku.solve()



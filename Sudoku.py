class Sudoku:

    def __init__(self, board:'list[list]') -> None:
        if (len(board) != 9 or len(board[0]) != 9): raise "Expected a 9 by 9 board"
        self.board = board
        self.iterations = []

    # for printing out the 2d list representation of the board
    def display(self, board:'list[list]'):
        if (len(board) != 9):
            print("Not a valid 9x9 sudoku board!")
            return
        x = 0
        for i in range(len(board)+4):
            if (i==0 or i==4 or i==8 or i==12):
                print('-------------------------')
                continue
            y = 0
            for j in range(len(board)+4):
                if (j == 0 or j==4 or j==8):
                    print('|', end=' ')
                elif (j == 12):
                    print('|')
                else:
                    print(board[x][y], end=' ')
                    y += 1
            x += 1

    # method to check if a certain number, n, is valid to be 
    # place at a certain x and y coordinate in the board
    def isPossible(self, x:int, y:int, n:int) -> bool:
        if (x > 8 and y > 8 and n >= 0 and n <= 9):
            return False
        #horizontal check
        for i in range(9):
            if (self.board[x][i] == n and i != y):
                return False
        #vertical check
        for i in range(9):
            if (self.board[i][y] == n and i != x):
                return False
        #square check
        square_x = x // 3
        square_y = y // 3
        for i in range(3):
            for j in range(3):
                if (self.board[square_x * 3 + i][square_y * 3 + j] == n and x != square_x * 3 + i and y != square_y * 3 + j):
                    return False
        #possible placement
        return True

    # Method to check if solution is correct
    def isSolution(self) -> bool:
        for i in range(9):
            for j in range(9):
                if (not(self.isPossible(self.board, i, j, self.board[i][j]))):
                    return False
        return True

    # Method to find the next empty coordinate in the board
    # Returns false if there are no empty space left (solved)
    def nextEmpty(self, loc:list) -> bool: 
        for i in range(9):
            for j in range(9):
                if (self.board[i][j] == '.'):
                    loc[0] = i
                    loc[1] = j
                    return True
        return False
    
    # Method to solve the board
    # Returns false if board is not solveable
    def solve(self) -> bool:
        loc = [0,0]
        if (not self.nextEmpty(loc)):
            return True
        i = loc[0]
        j = loc[1]
        for n in range(1,10):
            if (self.isPossible(i, j, n)):
                self.board[i][j] = n
                self.display(self.board)
                if (self.solve()):
                    return True
                self.board[i][j] = '.'
        return False





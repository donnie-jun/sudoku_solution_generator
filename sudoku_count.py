import random

class Sudoku:
    def __init__(self):
        self.count = 0
        
    def solveSudoku(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    choices = '123456789'
                    for n in choices:
                        block =  sum([board[(i//3)*3+x][(j//3)*3:(j//3)*3+3] for x in range(3)],[])
                        if n not in board[i] and n not in [board[t][j] for t in range(9)] and n not in block:
                            board[i][j] = n
                            self.solveSudoku(board)     
                    board[i][j]='.' 
                    return
        self.count += 1
        if self.count%100 == 0:
            print(self.count,end='\r')
        return
                    
generator = Sudoku()
Input = [['.']*9 for _ in range(9)]
generator.solveSudoku(Input)
print(generator.count)

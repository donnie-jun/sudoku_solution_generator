import random

class Sudoku:
    def __init__(self):
        self.results=[] # Storage for generated sudoku
        self.terminate = None # Define a exit point so the backtracking can stop
        
    def solveSudoku(self,board):
        """
        :type board: List[List[str]]
        :If board is all blank, all possiblities will be generated one by one
        :rtype: None.
        """
        if self.terminate: return 
        
        for i in range(9):
            for j in range(9): # This is just to find the first blank space, then return
                if board[i][j]=='.':
                    L = list('123456789')
                    random.shuffle(L) # Shuffle the choice list to get randomized sudoku
                    shuffled = ''.join(L)

                    # Backtracking sequence start here
                    for n in shuffled:
                        # The 3x3 check block is defined this way:
                        block =  sum([board[(i//3)*3+x][(j//3)*3:(j//3)*3+3] for x in range(3)],[])
                        # Check if the number does not exist in row, column, and block
                        if n not in board[i] and n not in [board[t][j] for t in range(9)] and n not in block:
                            board[i][j] = n # If legid, fill in this number
                            self.solveSudoku(board) # Continue backtracking with the newly filled number

                    # Reset this spot to continue looking for next permutation        
                    board[i][j]='.' 
                    return # Backtrack to previous node
                
        # If found a permutation, append to results
        self.results.append(board) 

        # Following is to print each found sudoku
        print('Sudoku num.{} found:'.format(len(self.results)))
        for i in board:
            print(i)
        print('\nEnter anything to terminate...')
        self.terminate = input()
        
        return
                    
             
generator = Sudoku()

# This Input can be your sudoku, or leave as
# all blank to generate all possible permutations
Input = [[".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         ]

generator.solveSudoku(Input)

## sudoku_solution_generator
This simple generator uses the minimum implementation of a backtracking algorithm to continuously generate random sudoku solutions.  
Another script (uncommented) sudoku_count.py simply continuously count solutions and print out number of solutions found.  

                 block =  sum([board[(i//3)*3+x][(j//3)*3:(j//3)*3+3] for x in range(3)],[])  
                 if n not in board[i] and n not in [board[t][j] for t in range(9)] and n not in block:  
                     board[i][j] = n  
                     self.solveSudoku(board)    
                              
Output:   
Sudoku num.1 found:   
['8', '5', '3', '9', '7', '4', '2', '6', '1']  
['9', '7', '4', '2', '6', '1', '5', '8', '3']  
['1', '6', '2', '8', '5', '3', '4', '7', '9']  
['5', '2', '1', '7', '9', '8', '6', '3', '4']  
['7', '9', '6', '3', '4', '5', '1', '2', '8']  
['4', '3', '8', '6', '1', '2', '9', '5', '7']  
['6', '8', '7', '4', '2', '9', '3', '1', '5']  
['2', '4', '5', '1', '3', '7', '8', '9', '6']  
['3', '1', '9', '5', '8', '6', '7', '4', '2']  
  
Enter anything to terminate...  
Sudoku num.2 found:  
['8', '5', '3', '9', '7', '4', '2', '6', '1']  
['9', '7', '4', '2', '6', '1', '5', '8', '3']  
['1', '6', '2', '8', '5', '3', '4', '7', '9']  
['5', '2', '1', '7', '9', '8', '6', '3', '4']  
['7', '9', '6', '3', '4', '5', '1', '2', '8']  
['4', '3', '8', '6', '1', '2', '9', '5', '7']  
['6', '8', '7', '4', '2', '9', '3', '1', '5']  
['2', '1', '9', '5', '3', '7', '8', '4', '6']  
['3', '4', '5', '1', '8', '6', '7', '9', '2']  
  
Enter anything to terminate...  
Sudoku num.3 found:  
['8', '5', '3', '9', '7', '4', '2', '6', '1']  
['9', '7', '4', '2', '6', '1', '5', '8', '3']  
['1', '6', '2', '8', '5', '3', '4', '7', '9']  
['5', '2', '1', '7', '9', '8', '6', '3', '4']  
['7', '9', '6', '3', '4', '5', '1', '2', '8']  
['4', '3', '8', '6', '1', '2', '9', '5', '7']  
['6', '8', '7', '4', '2', '9', '3', '1', '5']  
['3', '4', '5', '1', '8', '6', '7', '9', '2']  
['2', '1', '9', '5', '3', '7', '8', '4', '6']  
.  
.  
.  
By the way: From Wikipedia: The number of classic 9×9 Sudoku solution grids is 6,670,903,752,021,072,936,960, or approximately 6.67×10^21.  
So...if we get 1000 solutions per second, it takes only 211,504,312,532 years to get all of them. Let's start!

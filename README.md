# Sudoku-Solver
This program takes advantage of the sheer computational speed of computers to solve the given sudoku puzzle using the backtracking technique. The backtracking technique involves trying every valid number (1-9) in every empty cell, checking if the attempted number is valid in the given cell, and to backtrack if the attempted number is not valid for the cell. 

Input:
The puzzle is in the format of a 2D array making a 9x9 cell gird. The value are 1 to 9 for given values, and -1 for empty cells.

Output:
Prints a @D array of size 9x9 of the given solution.

Some advantages to this technique over the others are:
- The solution to the puzzle is guaranteed. (if the puzzle is valid)
- The solving time of the algorithm is unrelated to the difficulty of the puzzle.
- The algorithm is simpler than the other algorithms.

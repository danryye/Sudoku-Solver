def find_empty_cell(puzzle):
    # finds the row and column of the next empty cell
    # returns a row, col tuple, or (None, None) if it doesn't exist

    for r in range(9): # loops through puzzle
        for c in range(9):
            if puzzle[r][c] == -1: # checks for cell to be empty
                return r, c # empty cell is found

    return (None, None) # no empty cell found


def is_valid_guess(puzzle, guess, row, col):
    # Checks whether the guess at the cell at row, col is valid. This
    # will check the row, column, and 3x3 block the cell is in.
    # returns True if the cell position is valid, False otherwise

    # Check #1 - Checks the row
    row_values = puzzle[row]
    if guess in row_values:
        return False # The value already exists in the row, return False

    # Check #2 - Checks the column
    column_values = [puzzle[index][col] for index in range(9)]
    if guess in column_values:
        return False; # The value already exists in the column, return False

    # Check #3 - Checks the 3x3 box it's in
    row_start = (row // 3) * 3 # Starting row index of the 3x3 box
    col_start = (col // 3) * 3 # Starting col index of the 3x3 box

    # Loops through 3x3 box area to check for guess
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False # The value exists in the 3x3 box, returns False

    # The value has passed all the checks and is valid, returns True
    return True

def sudoku_solver(puzzle):
    # solves the given puzzle using the backtracking method
    # the puzzle is a 2d array, making a 9x9 grid with 81 cells
    # returns True if a solution exists, False otherwise
    # mutates the puzzle to the solution, if it exists

    # Starts by locating the first empty cell
    row, col = find_empty_cell(puzzle)

    # All cells are filled, the puzzle is solved
    if row is None:
        return True

    for guess in range(1, 10): # Loop of values 1 to 9
        if is_valid_guess(puzzle, guess, row, col): # checks if the value position is valid
            puzzle[row][col] = guess

            # Recursively calls the function to solve the rest of the puzzle
            if sudoku_solver(puzzle):
                return True

        # Reverts the index to -1 when the guess is not valid to check for
        # the guess in the iteration
        puzzle[row][col] = -1

    # If all indices are checked with values being invalid, the puzzle is
    # unsolvable. Therefore, returns False
    return False

if __name__ == "__main__":
    puzzle1 = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]
    ]

    print(puzzle1)
    print(sudoku_solver(puzzle1))
    print(puzzle1)
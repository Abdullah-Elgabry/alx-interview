#!/usr/bin/python3
""" NQuee task  N×N chessboard ##solved"""

from sys import argv


def is_valid_queen_placement(queens_positions: list) -> bool:
    """Check if the latest queen placement is valid.
    
    Args:
        queens_positions (list): List containing the column positions of queens 
                                 placed on the board so far.
    
    Returns:
        bool: True if the current queen placement is valid, False otherwise.
    """
    current_row = len(queens_positions) - 1
    for row in range(current_row):
        column_difference = abs(queens_positions[row] - queens_positions[current_row])
        if column_difference == 0 or column_difference == current_row - row:
            return False
    return True


def solve_n_queens(n: int, row: int, queens_positions: list, solutions: list):
    """Solve the N-Queens problem recursively and print each valid solution.
    
    Args:
        n (int): The size of the chessboard (n x n).
        row (int): The current row being processed.
        queens_positions (list): List containing the column positions of queens 
                                 placed on the board.
        solutions (list): List to store the current solution being built.
    """
    if row == n:
        print(solutions)
    else:
        for column in range(n):
            queens_positions.append(column)
            solutions.append([row, column])
            if is_valid_queen_placement(queens_positions):
                solve_n_queens(n, row + 1, queens_positions, solutions)
            queens_positions.pop()
            solutions.pop()


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n < 4:
    print('N must be at least 4')
    exit(1)
else:
    solve_n_queens(n, 0, [], [])

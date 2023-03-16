#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys
"""get access to some variables"""
def nqueens(n):
    """
    Initialize an `n`x`n`represents 
    the size of the board and the number of queens to be placed
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        """checks if a queen can be placed on a square in the current row,"""
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queen(board, row):
        """current state of the board and the current row being processed."""
        if row == n:
            print([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                place_queen(board, row+1)

    place_queen([0]*n, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

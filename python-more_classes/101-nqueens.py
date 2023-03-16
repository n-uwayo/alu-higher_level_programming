#!/usr/bin/python3

import sys

def nqueens(n):

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):

        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queen(board, row):

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

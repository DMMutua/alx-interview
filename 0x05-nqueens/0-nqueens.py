#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at the
    given row and column without attacking others"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def nqueens_util(N, row, board):
    """Utility to Print Directly"""
    if row == N:
        # All queens are placed, print the solution
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            nqueens_util(N, row + 1, board)


def nqueens(N):
    """Main Solver Function"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    nqueens_util(N, 0, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])

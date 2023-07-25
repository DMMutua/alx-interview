#!/usr/bin/env python3
"""Solving the N Queens Challenge"""


import sys

def is_safe(board, row, col, N):
    """Check if a queen can be placed at the given
    position without attacking others"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def nqueens_helper(board, row, N):
    """Helper Function"""
    if row == N:
        # All queens have been placed, print the solution
        for i in range(N):
            print("[{}, {}]".format(i, board[i]))
        print()
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            nqueens_helper(board, row + 1, N)
            board[row] = -1  # Backtrack

def nqueens(N):
    """Major Function to Solve Problem"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    nqueens_helper(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)


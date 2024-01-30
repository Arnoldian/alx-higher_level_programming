#!/usr/bin/pyhon3
"""
Module for N-queens puzzle
"""
import sys


def no_risk(board, row, col, N, result):
    """method for evaluating risk"""
    for i in range(col):
        if board[row][i] == 1:
            return (False)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return (False)
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return (False)
    return (True)

def solve_n_queens(board, col, N, result):
    """method for solving"""
    if col >= N:
        temp = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    temp.append([i, j])
        result.append(temp)
        return False
    res = False
    for i in range(N):
        if is_safe(board, i, col, N, result):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1, N, result) or res
            board[i][col] = 0
    return (res)

if __name__ == "__main__":
    """method for name"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    solve_n_queens(board, 0, N, result)
    for res in result:
        print(res)

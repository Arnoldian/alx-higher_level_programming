#!/usr/bin/python3
"""
Module for N-queens puzzle
"""
import sys


def start_board(n):
    """method for starting board"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """method for board copy"""
    if isinstance(board, list):
        return (list(map(board_deepcopy, board)))

    return (board)


def get_solution(board):
    """method for solution"""
    solution = []

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break

    return (solution)


def xout(board, row, col):
    """method xout for exing out spots"""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1

    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1

    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1

    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1

    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_w_recursion(board, row, queens, solutions):
    """method for solving recursively"""
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = solve_w_recursion(tmp_board, row + 1,
                                        queens + 1, solutions)
    return (solutions)


if __name__ == "__main__":
    """outputing the result"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = start_board(int(sys.argv[1]))
    solutions = solve_w_recursion(board, 0, 0, [])

    for sol in solutions:
        print(sol)

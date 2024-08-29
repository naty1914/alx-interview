#!/usr/bin/python3
"""A module that provides solutions for N queens problem """
import sys


def print_error(message):
    """It print the error message and exit with status 1"""
    print(message)
    sys.exit(1)


def check_safe(board, row, col):
    """A function that checks if it is safe to place a queen
    at board[row][col]"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def get_solution(board, row, num):
    """A function that prints a solution to the N queens problem"""
    if row == num:
        solution = [[i, board[i]] for i in range(num)]
        print(solution)
        return
    for col in range(num):
        if check_safe(board, row, col):
            board[row] = col
            get_solution(board, row + 1, num)


def main():
    """It's the main function that handles the input and output"""
    if len(sys.argv) != 2:
        print_error("Usage: nqueens N")
    try:
        num = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")
    if num < 4:
        print_error("N must be at least 4")
    board = [-1] * num
    get_solution(board, 0, num)


if __name__ == '__main__':
    main()

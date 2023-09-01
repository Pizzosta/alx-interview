#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if it's safe to place a queen at the given position
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the diagonals
    for i in range(row, -1, -1):
        for j in range(col, -1, -1):
            if i == row and j == col:
                continue
            if board[i][j] == 1 and abs(row - i) == abs(col - j):
                return False

    for i in range(row, N):
        for j in range(col, -1, -1):
            if i == row and j == col:
                continue
            if board[i][j] == 1 and abs(row - i) == abs(col - j):
                return False

    return True


def solve_nqueens(board, col, N, solutions):
    # Recursive function to find solutions to the N Queens problem
    if col >= N:
        solutions.append([row.index(1) for row in board])
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, col + 1, N, solutions)
            board[row][col] = 0  # Backtrack


def print_solution(solution):
    formatted_solution = "["
    for idx, pos in enumerate(solution):
        if idx == len(solution) - 1:
            formatted_solution += "[{}, {}]".format(pos, solution[pos])
        else:
            formatted_solution += "[{}, {}], ".format(pos, solution[pos])
    formatted_solution += "]"
    print(formatted_solution)


def main():
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

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print_solution(solution)


if __name__ == "__main__":
    main()

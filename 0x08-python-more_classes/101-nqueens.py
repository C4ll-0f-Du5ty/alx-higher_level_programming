#!/usr/bin/python3
# def solve_n_queens(N):
#     def can_place(pos, ocuppied_positions):
#         for i in range(ocuppied_positions):
#             if pos[i] == pos[ocuppied_positions] or \
#                 pos[i] - pos[ocuppied_positions] ==
#                   i - ocuppied_positions or \
#                 pos[i] - pos[ocuppied_positions] == ocuppied_positions - i:
#                 return False
#         return True

#     def place_queens(N, pos, ocuppied_positions):
#         if ocuppied_positions == N:
#             print(pos)
#             return
#         for i in range(N):
#             pos[ocuppied_positions] = i
#             if can_place(pos, ocuppied_positions):
#                 place_queens(N, pos, ocuppied_positions + 1)

#     pos = [0] * N
#     place_queens(N, pos, 0)

# # Test the function
# solve_n_queens(4)


import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    print_solutions(solutions)


if __name__ == "__main__":

    main()

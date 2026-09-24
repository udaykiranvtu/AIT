# N-Queen Problem using Constraint Satisfaction

N = 8

board = [[0 for _ in range(N)] for _ in range(N)]


def is_safe(row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True


def solve(row):

    # All queens are placed
    if row == N:
        return True

    # Try every column
    for col in range(N):

        if is_safe(row, col):

            # Place queen
            board[row][col] = 1

            # Solve next row
            if solve(row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


if solve(0):

    print("Solution for 8-Queens Problem:")

    for row in board:
        print(row)

else:
    print("No solution found")
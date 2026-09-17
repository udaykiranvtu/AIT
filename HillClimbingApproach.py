#Approach:
#1.current-state
# 2.compare with neighbour nodes
# 3.if higher than current state->move there
# 4.repeat until neither  neighbours higher


# Hill Climbing Algorithm
# Treasure Hunt Game

grid = [
    [2, 4, 5, 5, 3],
    [3, 6, 7, 8, 4],
    [1, 5, 7, 10, 6],
    [2, 4, 6, 8, 5]
]

rows = len(grid)
cols = len(grid[0])

# Starting position
current_row = 0
current_col = 0

print("TREASURE HUNT - HILL CLIMBING")
print("--------------------------------")

print("Starting position:",
      (current_row, current_col))
print("Initial value:",
      grid[current_row][current_col])

while True:

    current_value = grid[current_row][current_col]

    # Possible moves: Up, Down, Left, Right
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    best_row = current_row
    best_col = current_col
    best_value = current_value

    # Check all neighboring states
    for dr, dc in moves:

        new_row = current_row + dr
        new_col = current_col + dc

        # Check whether position is inside grid
        if 0 <= new_row < rows and 0 <= new_col < cols:

            value = grid[new_row][new_col]

            if value > best_value:
                best_value = value
                best_row = new_row
                best_col = new_col

    # Stop if no better neighboring state exists
    if best_value <= current_value:
        print("\nNo better neighboring state found.")
        print("Hill Climbing stopped.")
        break

    # Set new current state
    current_row = best_row
    current_col = best_col

    print("Moved to:",
          (current_row, current_col),
          "Value:", best_value)

print("\nFinal Position:",
      (current_row, current_col))

print("Maximum Treasure Found:",
      grid[current_row][current_col])




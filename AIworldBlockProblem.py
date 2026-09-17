# Blocks World Problem
# Goal: Place Block A onto Block B

# Initial state
A = "Table"
B = "Table"
hand = "Empty"

print("Initial State:")
print("Block A:", A)
print("Block B:", B)
print("Robot Hand:", hand)

# Action 1: Pickup A
def pickup(block):
    global hand

    if block == "A" and A == "Table" and hand == "Empty":
        hand = "A"
        print("\nAction: PICKUP(A)")
        print("Robot picked up Block A.")
    else:
        print("\nPickup failed.")


# Action 2: Putdown A
def putdown(block):
    global hand, A

    if block == "A" and hand == "A":
        A = "Table"
        hand = "Empty"
        print("\nAction: PUTDOWN(A)")
        print("Robot placed Block A on the table.")
    else:
        print("\nPutdown failed.")


# Action 3: Stack A on B
def stack(block1, block2):
    global hand, A

    if block1 == "A" and block2 == "B" and hand == "A":
        A = "B"
        hand = "Empty"
        print("\nAction: STACK(A,B)")
        print("Block A is placed on Block B.")
    else:
        print("\nStack failed.")


# Action 4: Unstack A from B
def unstack(block1, block2):
    global hand, A

    if block1 == "A" and block2 == "B" and A == "B" and hand == "Empty":
        hand = "A"
        A = "Table"
        print("\nAction: UNSTACK(A,B)")
        print("Block A is removed from Block B.")
    else:
        print("\nUnstack failed.")


# Solve the problem
pickup("A")
stack("A", "B")

# Final state
print("\nFinal State:")
print("Block A:", A)
print("Block B:", B)
print("Robot Hand:", hand)

if A == "B":
    print("\nGoal Achieved: Block A is placed on Block B.")
else:
    print("\nGoal Not Achieved.")
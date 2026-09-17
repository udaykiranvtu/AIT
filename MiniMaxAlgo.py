class Node:
    def __init__(self, name, value=None,children=None):
        self.name = name
        self.value = value
        self.children = children if children is not None else []

    def is_terminal(self):
        return len(self.children) == 0

def minimax(node, depth, is_maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.value
    if is_maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            evaluation = minimax(child, depth-1, False)
            max_eval = max(max_eval,evaluation)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            evaluation = minimax(child, depth-1, True)
            min_eval = min(min_eval,evaluation)
        return min_eval
leaf_A = Node("A",value=3)
leaf_B = Node("B",value=5)
leaf_C = Node("C",value=2)
leaf_D = Node("D",value=9)
leaf_E = Node("E",value=12)
leaf_F = Node("F",value=5)
leaf_G = Node("G",value=23)
leaf_H = Node("H",value=23)

child_node_1 = Node("child_1",children=[leaf_A,leaf_B])
child_node_2 = Node("child_2",children=[leaf_C,leaf_D])
child_node_3 = Node("child_3",children=[leaf_E,leaf_F])
child_node_4 = Node("child_4",children=[leaf_G,leaf_H])

branch_left = Node("Branch_left",children=[child_node_1,child_node_2])
branch_right = Node("Branch_right",children=[child_node_3,child_node_4])

root = Node("Root", children=[branch_left,branch_right])

optimal_value = minimax(root, depth=3, is_maximizing_player=True)
print(f"The optimal Value at the Root node is: {optimal_value}")
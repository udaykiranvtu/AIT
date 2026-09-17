# CSP - Graph Coloring using Backtracking
# User enters number of vertices.
# User enters number of edges.
# User enters the connections/edges.
# User enters the maximum number of colors available.
# The program uses Backtracking CSP to assign colors.
# It also finds the minimum number of colors required (chromatic number).
# Finally, it prints the color assigned to every vertex.

def is_safe(vertex, color, graph, colors):


    for neighbour in graph[vertex]:
        if colors[neighbour] == color:
            return False

    return True


def solve_csp(vertex, n, max_colors, graph, colors):


    # If all vertices have been colored
    if vertex == n:
        return True

    # Try every available color
    for color in range(1, max_colors + 1):

        # Check whether this color can be assigned
        if is_safe(vertex, color, graph, colors):

            # Assign color
            colors[vertex] = color

            # Recursively color the next vertex
            if solve_csp(vertex + 1, n, max_colors, graph, colors):
                return True

            # Backtrack
            colors[vertex] = 0

    return False


def find_minimum_colors(n, graph, max_colors):


    for number_of_colors in range(1, max_colors + 1):

        colors = [0] * n

        if solve_csp(0, n, number_of_colors, graph, colors):
            return number_of_colors, colors

    return None, None


# ---------------- MAIN PROGRAM ----------------

print("===== CSP GRAPH COLORING =====")

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Create graph
graph = [[] for _ in range(n)]

# Input number of edges
edges = int(input("Enter number of edges: "))

print("\nEnter the edges:")
print("Example: 0 1 means vertex 0 is connected to vertex 1")

for i in range(edges):
    u, v = map(int, input(f"Edge {i + 1}: ").split())

    # Add connection in both directions
    graph[u].append(v)
    graph[v].append(u)

# Maximum colors user is willing to use
max_colors = int(input("\nEnter maximum number of colors available: "))

# Find minimum colors
minimum_colors, solution = find_minimum_colors(
    n, graph, max_colors
)

# Display result
print("\n===== RESULT =====")

if minimum_colors is None:
    print("Graph cannot be colored using", max_colors, "colors.")

else:
    print("Minimum number of colors required:", minimum_colors)

    print("\nVertex Coloring:")

    for vertex in range(n):
        print(
            "Vertex", vertex,
            "-> Color", solution[vertex]
        )

    print("\nGraph successfully colored!")
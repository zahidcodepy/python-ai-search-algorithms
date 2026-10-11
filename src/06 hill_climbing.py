"""
Experiment 06 — Hill Climbing
Subject: Artificial Intelligence / Python Practical

Aim:
    To write and execute a Python program that implements the Simple Hill
    Climbing algorithm to search for a locally optimal node using
    heuristic values.

Description:
    Hill Climbing is a local search algorithm. Starting from an initial
    node, it repeatedly moves to the single best neighbouring node
    according to a heuristic function h(n). In this minimization version,
    "best" means the neighbour with the lowest h(n). The algorithm stops
    as soon as no neighbour improves on the current node's heuristic value
    — at that point it has reached a peak (here, a local minimum) in the
    search space, whether or not that peak is the best possible solution.
"""

# Graph represented as an adjacency list (dictionary of lists)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic values h(n) — lower is considered better (closer to the goal)
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 2
}


def hill_climbing(graph, heuristic, start):
    """
    Perform Simple Hill Climbing from a start node.

    Parameters:
        graph (dict): Adjacency list representation of the graph.
        heuristic (dict): Heuristic value h(n) for each node.
        start (str): The node to start the climb from.

    Returns:
        list: The sequence of nodes visited, ending at the local optimum.
    """
    current = start
    path = [current]

    while True:
        neighbours = graph[current]

        # No neighbours to move to — current node is the end of the path
        if not neighbours:
            break

        # Pick the neighbour with the lowest (best) heuristic value
        next_node = min(neighbours, key=lambda node: heuristic[node])

        # Stop if the best neighbour is not actually better than the
        # current node — this is the local optimum stopping condition
        if heuristic[next_node] >= heuristic[current]:
            break

        current = next_node
        path.append(current)

    return path


# Driver code
if __name__ == "__main__":
    start = 'A'
    result = hill_climbing(graph, heuristic, start)

    print("Hill Climbing Path:")
    print(" -> ".join(result))
    print("Final Heuristic Value:", heuristic[result[-1]])

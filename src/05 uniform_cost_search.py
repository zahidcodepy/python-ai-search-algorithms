"""
Experiment 05 — Uniform Cost Search (UCS)
Subject: Artificial Intelligence / Python Practical

Aim:
    To write and execute a Python program that implements the Uniform Cost
    Search algorithm to find the lowest-cost path in a weighted graph.

Description:
    Uniform Cost Search is an uninformed search algorithm that always
    expands the node with the lowest cumulative path cost g(n) from the
    start node. A priority queue (min-heap) keeps the frontier ordered by
    cost, and a visited set prevents a node from being expanded twice.
    Because the cheapest node is always expanded first, the first time the
    goal is removed from the queue, the path found is a lowest-cost path
    (edge costs must be non-negative).
"""

import heapq

# Weighted graph as an adjacency list: node -> list of (neighbour, edge_cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1), ('E', 6)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'G': []
}


def uniform_cost_search(graph, start, goal):
    """
    Find the lowest-cost path from start to goal using Uniform Cost Search.

    Parameters:
        graph (dict): Weighted adjacency list {node: [(neighbour, cost), ...]}.
        start (str): The node to start the search from.
        goal (str): The target node to search for.

    Returns:
        tuple: (path, total_cost). Returns (None, None) if the goal is
        not reachable from the start node.
    """
    # Priority queue stores tuples of (cumulative_cost, node, path_so_far)
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        # Pop the node with the lowest cumulative cost
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        # The first time the goal is popped, its path is the cheapest one
        if node == goal:
            return path, cost

        # Push unvisited neighbours with their updated cumulative cost
        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + edge_cost, neighbour, path + [neighbour])
                )

    return None, None


# Driver code
if __name__ == "__main__":
    start = 'A'
    goal = 'G'
    path, total_cost = uniform_cost_search(graph, start, goal)

    print("Uniform Cost Search Path:")
    print(" -> ".join(path))
    print("Total Cost:", total_cost)

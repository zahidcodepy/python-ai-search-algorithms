"""
Experiment 04 — Best First Search
Subject: Artificial Intelligence / Python Practical

Aim:
    To write and execute a Python program that implements the Best First
    Search algorithm using heuristic values to select the most promising
    node during graph traversal.

Description:
    Best First Search is an informed search technique. It selects the next
    node to explore based on an evaluation value — here, the heuristic
    h(n). In this greedy version, the node with the smallest heuristic
    value is always chosen first. A priority queue (min-heap) keeps
    available nodes ordered by heuristic value, and a visited set prevents
    the same node from being processed more than once.
"""

import heapq

# Graph represented as an adjacency list (dictionary of lists)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values h(n) — estimated distance/cost from each node to the goal
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 7,
    'E': 3,
    'F': 1,
    'G': 0
}


def best_first_search(graph, heuristic, start, goal):
    """
    Perform a Greedy Best First Search on a graph using heuristic values.

    Parameters:
        graph (dict): Adjacency list representation of the graph.
        heuristic (dict): Heuristic value h(n) for each node.
        start (str): The node to start the search from.
        goal (str): The target node to search for.

    Returns:
        list: The order in which nodes were visited (the traversal path).
    """
    # Priority queue stores tuples of (heuristic_value, node)
    priority_queue = [(heuristic[start], start)]
    visited = set()
    traversal = []

    while priority_queue:
        # Pop the node with the smallest heuristic value
        h_value, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        traversal.append(node)

        # Stop as soon as the goal node is reached
        if node == goal:
            break

        # Push unvisited neighbours into the priority queue
        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbour], neighbour)
                )

    return traversal


# Driver code
if __name__ == "__main__":
    start = 'A'
    goal = 'G'
    result = best_first_search(graph, heuristic, start, goal)

    print("Best First Search Traversal:")
    print(" -> ".join(result))

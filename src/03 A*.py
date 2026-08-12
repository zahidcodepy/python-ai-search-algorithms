"""
A* Search
-----------
Informed search algorithm that finds the shortest path using
f(n) = g(n) + h(n), where g(n) is the cost so far and h(n) is a
heuristic estimate of the cost to the goal.

Docs: docs/astar.md
"""

import heapq


def astar(graph, start, goal, heuristic):
    """
    Perform an A* Search on a weighted `graph` from `start` to `goal`.

    Args:
        graph (dict): Adjacency list with edge weights, e.g.
                       {"A": [("B", 1), ("C", 2)], ...}
        start (str): Starting node.
        goal (str): Target node.
        heuristic (dict): Estimated cost from each node to the goal,
                           e.g. {"A": 4, "B": 2, ...}

    Returns:
        tuple(list, float) | tuple(None, float('inf')):
            The optimal path and its total cost, or (None, inf) if
            no path exists.
    """
    open_set = [(heuristic[start], start)]  # (f_score, node)
    came_from = {}

    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0

    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic[start]

    open_set_nodes = {start}

    while open_set:
        _, current = heapq.heappop(open_set)
        open_set_nodes.discard(current)

        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        for neighbor, weight in graph.get(current, []):
            tentative_g = g_score[current] + weight

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic.get(neighbor, 0)

                if neighbor not in open_set_nodes:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_nodes.add(neighbor)

    return None, float("inf")


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def print_path(path, cost):
    if path:
        print(" -> ".join(path))
        print(f"Total cost: {cost}")
    else:
        print("No path found.")


if __name__ == "__main__":
    # Sample weighted graph (matches the example in docs/astar.md)
    graph = {
        "A": [("B", 1), ("C", 2)],
        "B": [("A", 1), ("D", 2)],
        "C": [("A", 2), ("E", 1)],
        "D": [("B", 2), ("E", 1)],
        "E": [("C", 1), ("D", 1)],
    }

    # Heuristic: straight-line/estimated distance to goal "E"
    heuristic = {
        "A": 4,
        "B": 3,
        "C": 1,
        "D": 1,
        "E": 0,
    }

    start_node = "A"
    goal_node = "E"

    print(f"Running A* Search from '{start_node}' to '{goal_node}'...\n")
    result_path, result_cost = astar(graph, start_node, goal_node, heuristic)

    print("Path found:")
    print_path(result_path, result_cost)

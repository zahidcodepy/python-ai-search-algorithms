"""
Breadth First Search (BFS)
---------------------------
Explores a graph level by level using a queue (FIFO), guaranteeing the
shortest path in terms of number of edges for unweighted graphs.

Docs: docs/bfs.md
"""

from collections import deque


def bfs(graph, start, goal):
    """
    Perform a Breadth First Search on `graph` from `start` to `goal`.

    Args:
        graph (dict): Adjacency list, e.g. {"A": ["B", "C"], ...}
        start (str): Starting node.
        goal (str): Target node.

    Returns:
        list | None: The path from start to goal as a list of nodes,
                      or None if no path exists.
    """
    visited = {start}
    queue = deque([[start]])  # queue of paths, not just nodes

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


def print_path(path):
    if path:
        print(" -> ".join(path))
    else:
        print("No path found.")


if __name__ == "__main__":
    # Sample graph (matches the example in docs/bfs.md)
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "E"],
        "E": ["C", "D"],
    }

    start_node = "A"
    goal_node = "E"

    print(f"Running BFS from '{start_node}' to '{goal_node}'...\n")
    result_path = bfs(graph, start_node, goal_node)

    print("Path found:")
    print_path(result_path)

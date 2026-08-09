"""
Depth First Search (DFS)
--------------------------
Explores as far as possible along each branch before backtracking,
using recursion (the call stack) to track the current path.

Docs: docs/dfs.md
"""


def dfs(graph, node, goal, visited=None, path=None):
    """
    Perform a recursive Depth First Search on `graph` from `node` to `goal`.

    Args:
        graph (dict): Adjacency list, e.g. {"A": ["B", "C"], ...}
        node (str): Current node being visited.
        goal (str): Target node.
        visited (set): Nodes already visited (used internally for recursion).
        path (list): Path taken so far (used internally for recursion).

    Returns:
        list | None: The path from the original start node to goal,
                      or None if no path exists.
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path = path + [node]

    if node == goal:
        return path

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result is not None:
                return result

    return None


def print_path(path):
    if path:
        print(" -> ".join(path))
    else:
        print("No path found.")


if __name__ == "__main__":
    # Sample graph (matches the example in docs/dfs.md)
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "E"],
        "E": ["C", "D"],
    }

    start_node = "A"
    goal_node = "E"

    print(f"Running DFS from '{start_node}' to '{goal_node}'...\n")
    result_path = dfs(graph, start_node, goal_node)

    print("Path found:")
    print_path(result_path)

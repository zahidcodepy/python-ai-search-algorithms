# Depth First Search (DFS)

[← Back to README](../README.md)

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Algorithm Steps](#algorithm-steps)
- [Pseudocode](#pseudocode)
- [Implementation](#implementation)
- [Example](#example)
- [Complexity Analysis](#complexity-analysis)
- [Use Cases](#use-cases)
- [Advantages & Limitations](#advantages--limitations)

---

## Overview

**Depth First Search (DFS)** is an uninformed graph traversal algorithm that explores as far as possible along each branch before backtracking. Unlike BFS, which expands level by level, DFS dives deep into a single path first, making it well-suited for problems involving exhaustive exploration, such as maze solving or topological sorting.

---

## How It Works

DFS uses a **stack** data structure — either explicitly or via recursion (the call stack) — to keep track of the path being explored. It visits a node, marks it as visited, then recursively (or iteratively) visits an unvisited neighbor, repeating this process until it hits a dead end, at which point it backtracks.

---

## Algorithm Steps

1. Start at the source node and mark it as visited.
2. Visit an unvisited neighbor of the current node and recurse into it.
3. If a node has no unvisited neighbors, backtrack to the previous node.
4. Repeat until all reachable nodes have been visited or the goal is found.

---

## Pseudocode

```text
DFS(graph, node, visited, goal):
    mark node as visited

    if node == goal:
        return path to node

    for neighbor in graph[node]:
        if neighbor not in visited:
            result = DFS(graph, neighbor, visited, goal)
            if result is not failure:
                return result

    return failure
```

---

## Implementation

The full implementation is available at [`src/dfs.py`](../src/dfs.py).

```bash
python src/dfs.py
```

---

## Example

**Graph:**

```text
A - B - D
|       |
C - - - E
```

**Traversal order starting from A (depth-first):** `A → B → D → E → C`

DFS commits to exploring one branch fully before backtracking, which can produce a very different visiting order compared to BFS.

---

## Complexity Analysis

| Metric | Complexity |
|--------|:----------:|
| Time Complexity | O(V + E) |
| Space Complexity | O(V) |

Where **V** is the number of vertices and **E** is the number of edges in the graph. Space complexity depends on the maximum depth of recursion (or explicit stack size).

---

## Use Cases

- Maze and puzzle solving
- Topological sorting of directed acyclic graphs (DAGs)
- Detecting cycles in a graph
- Pathfinding in game trees and decision trees

---

## Advantages & Limitations

**Advantages**
- Lower memory usage than BFS for deep, narrow graphs
- Naturally suited to recursive problem formulations

**Limitations**
- Does not guarantee the shortest path
- Can get trapped exploring very deep or infinite branches without a depth limit

---

[← Back to README](../README.md)

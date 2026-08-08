# Breadth First Search (BFS)

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

**Breadth First Search (BFS)** is an uninformed graph traversal algorithm that explores a graph level by level, starting from a given source node. It visits all neighbors of a node before moving on to their neighbors, which guarantees the shortest path in terms of number of edges for unweighted graphs.

BFS is one of the foundational algorithms in Artificial Intelligence search theory and forms the basis for understanding more advanced informed search strategies such as A*.

---

## How It Works

BFS uses a **queue (FIFO)** data structure to keep track of nodes to visit next. It starts at the root/source node, adds it to the queue, and then repeatedly dequeues a node, visits it, and enqueues all of its unvisited neighbors.

This level-by-level expansion ensures that nodes closer to the source are visited before nodes farther away.

---

## Algorithm Steps

1. Add the starting node to a queue and mark it as visited.
2. While the queue is not empty:
   - Dequeue the front node.
   - Process/visit the node (e.g., check if it is the goal).
   - Enqueue all unvisited neighbors of the node and mark them as visited.
3. Repeat until the queue is empty or the goal is found.

---

## Pseudocode

```text
BFS(graph, start, goal):
    create empty queue Q
    create empty visited set
    add start to Q
    add start to visited

    while Q is not empty:
        node = Q.dequeue()

        if node == goal:
            return path to node

        for neighbor in graph[node]:
            if neighbor not in visited:
                mark neighbor as visited
                enqueue neighbor into Q

    return failure
```

---

## Implementation

The full implementation is available at [`src/bfs.py`](../src/bfs.py).

```bash
python src/bfs.py
```

---

## Example

**Graph:**

```text
A - B - D
|       |
C - - - E
```

**Traversal order starting from A:** `A → B → C → D → E`

Each node is visited once, and nodes are explored in the order they are discovered — guaranteeing the shortest unweighted path to any reachable node.

---

## Complexity Analysis

| Metric | Complexity |
|--------|:----------:|
| Time Complexity | O(V + E) |
| Space Complexity | O(V) |

Where **V** is the number of vertices and **E** is the number of edges in the graph.

---

## Use Cases

- Finding the shortest path in an unweighted graph
- Web crawlers exploring linked pages
- Social network "degrees of connection" analysis
- Peer-to-peer network broadcasting

---

## Advantages & Limitations

**Advantages**
- Guarantees the shortest path in unweighted graphs
- Simple and predictable memory access pattern

**Limitations**
- Can consume significant memory for wide/large graphs
- Does not account for edge weights — unsuitable for weighted shortest-path problems

---

[← Back to README](../README.md)


# Hill Climbing

## Experiment Information

- **Experiment Number:** 06
- **Subject:** Artificial Intelligence / Python Practical
- **Aim:** To write and execute a Python program that implements the Simple Hill Climbing algorithm to search for a locally optimal node using heuristic values.
- **Programming Language:** Python 3
- **Algorithm:** Simple Hill Climbing (Local, Heuristic Search)

## Objective

The objective is to understand how a local search algorithm improves a solution step by step by always moving toward the best immediate neighbour, and why this can get stuck at a point that is only locally — not globally — optimal.

## Introduction

Hill Climbing is one of the simplest search strategies in AI. It can be pictured as climbing a hill in fog: at every step you can only see your immediate surroundings, so you always take a step toward higher ground (or, as implemented here, toward lower heuristic value) and stop once no nearby step helps. It keeps no memory of the path and never backtracks.

## Theory

- Hill Climbing is a **local search** algorithm — it does not explore the whole search space, only the current node and its immediate neighbours.
- It uses a heuristic function h(n) to evaluate how good each neighbour is.
- At every step, it moves to the single best neighbour of the current node.
- It has **no memory** of earlier nodes and **does not backtrack** — once it moves forward, it never reconsiders an earlier node.
- The search stops when no neighbour improves on the current node. This point is called a **local optimum**, and it is not guaranteed to be the best solution in the entire search space (the **global optimum**).

## How Hill Climbing Works

1. Start at the initial node.
2. Evaluate all neighbours of the current node using h(n).
3. Pick the neighbour with the best (here, lowest) heuristic value.
4. If that neighbour is better than the current node, move to it.
5. If no neighbour is better, stop — the current node is a local optimum.
6. Repeat steps 2–5 until the algorithm stops.

## Heuristic Function

h(n) estimates how close node `n` is to the goal. In this minimization version, a **lower h(n)** is better.

| Node | h(n) |
|------|------|
| A | 5 |
| B | 3 |
| C | 4 |
| D | 6 |
| E | 1 |
| F | 2 |

## Graph Used

**Nodes:** A, B, C, D, E, F

**Edges (directed):**
- A → B, C
- B → D, E
- C → F

**Start node:** A

```
            A (5)
           /     \
        B (3)    C (4)
       /   \        \
    D (6) E (1)     F (2)
```

![Hill Climbing Graph](../images/hill-climbing/hill-climbing-graph.png)

*The path taken by the algorithm (A → B → E) is highlighted in red.*

## Algorithm

1. Set the current node to the start node.
2. Get the neighbours of the current node.
3. If there are no neighbours, stop.
4. Find the neighbour with the best (lowest) heuristic value.
5. If that neighbour's heuristic value is not better than the current node's, stop — a local optimum has been reached.
6. Otherwise, move to that neighbour and repeat from step 2.

## Python Implementation

The full implementation is available at [`../src/hill_climbing.py`](../src/hill_climbing.py).

**Key parts of the code:**
- `min(neighbours, key=lambda node: heuristic[node])` selects the best neighbour in one step, with no explicit sorting or queue needed.
- The stopping condition `heuristic[next_node] >= heuristic[current]` is what makes this a *hill climbing* search rather than a full traversal — it refuses to move sideways or backward.
- No `visited` set is needed, because the algorithm never revisits a node.

## Execution

Run the program from the repository root:

```
python src/hill_climbing.py
```

## Expected Output

```
Hill Climbing Path:
A -> B -> E
Final Heuristic Value: 1
```

## Step-by-Step Execution

| Step | Current Node | Neighbours (h) | Best Neighbour | Decision |
|------|---------------|------------------|------------------|----------|
| 1 | A (h=5) | B (3), C (4) | B (3) | 3 < 5 → move to B |
| 2 | B (h=3) | D (6), E (1) | E (1) | 1 < 3 → move to E |
| 3 | E (h=1) | — | — | No neighbours → stop |

The algorithm starts at `A` and always steps toward the neighbour with the lowest heuristic value. It reaches `E`, whose heuristic value (1) is the lowest in the entire graph for this path, so in this particular example the local optimum found is also the best possible outcome.

## Time Complexity

In the worst case, Hill Climbing examines every neighbour of every node it visits before stopping, giving a time complexity of **O(V + E)** for a single run, where V is the number of vertices and E is the number of edges — similar to a single-path graph traversal, since no node is revisited.

## Space Complexity

**O(1)** additional space for the search itself, since only the current node and its neighbours need to be considered at any time (beyond the path list kept here for reporting purposes, which is O(V) in the worst case).

## Advantages

- Simple to understand and implement.
- Uses very little memory, since it does not need to store the whole search tree.
- Can find a solution quickly when the search space is well-behaved.

## Disadvantages

- Can get stuck at a **local optimum** that is not the best overall solution.
- Can get stuck on a **plateau**, a flat region where neighbouring nodes have equal heuristic values.
- Can get stuck at a **ridge**, where the optimal direction requires more than one single step to reach.
- Has no memory of the search, so it cannot backtrack if it takes a wrong step.
- Not guaranteed to find the global optimum or even a goal node.

## Applications

- Optimization problems with a well-defined, improvable objective
- Scheduling and resource allocation
- Neural network weight tuning (as a conceptual basis for gradient-based methods)
- Circuit design and layout problems
- Any problem where small, incremental improvements are meaningful

## Hill Climbing vs Best First Search

| Feature | Hill Climbing | Best First Search |
|---------|----------------|---------------------|
| Explores | Only the current node's neighbours | All frontier nodes seen so far |
| Data structure | None (single current node) | Priority queue |
| Backtracking | No | Effectively yes, via the frontier |
| Memory usage | Very low | Higher — keeps the whole frontier |
| Optimality | Not guaranteed — can get stuck locally | Not guaranteed, but explores more broadly |

## Viva Questions

1. **What is Hill Climbing?**
   It is a local search algorithm that always moves from the current node to the best neighbouring node, stopping when no neighbour is better.

2. **What is a local optimum?**
   A point where no neighbouring node improves on the current node, but which may not be the best solution in the whole search space.

3. **Does Hill Climbing backtrack?**
   No. It has no memory of previous nodes and never reconsiders an earlier decision.

4. **What are the main problems with Hill Climbing?**
   Getting stuck at a local optimum, a plateau, or a ridge.

5. **What is a plateau in Hill Climbing?**
   A flat area of the search space where neighbouring nodes have equal heuristic values, giving the algorithm no clear direction to move.

6. **Is Hill Climbing guaranteed to find the best solution?**
   No. It stops at the first local optimum it reaches, which may not be the global optimum.

7. **What is the space complexity of Hill Climbing, and why is it low?**
   O(1) for the core search, because it only needs to track the current node and its immediate neighbours, unlike algorithms that maintain a full frontier.

8. **What is the difference between Hill Climbing and Best First Search?**
   Hill Climbing only ever looks at the current node's neighbours and cannot backtrack; Best First Search keeps a priority queue of the entire frontier and can effectively backtrack by picking any previously discovered node.

## Conclusion

Simple Hill Climbing was implemented in Python using a heuristic function that always moves toward the best available neighbour. The experiment demonstrates both the strength of the approach — reaching a good solution quickly with minimal memory — and its key weakness, since the algorithm stops permanently as soon as it reaches any local optimum, without verifying whether a better solution exists elsewhere in the graph.

"""
Experiment 07 — AO* Search
Subject: Artificial Intelligence / Python Practical

Aim:
    To write and execute a Python program that implements the AO* algorithm
    to find the lowest-cost solution graph in an AND-OR graph.

Description:
    AO* is an informed search algorithm for AND-OR graphs, which are used
    to model problems that can be broken down into sub-problems.

        - An OR option means "solve ONE of these children".
        - An AND option means "solve ALL of these children".

    AO* repeatedly expands an unsolved node on the current best partial
    solution, calculates the cost of each of its options as
    sum(edge_cost + h(child)), keeps the cheapest option, and then revises
    (back-propagates) the costs of its ancestors. Because an estimate can
    turn out to be wrong, the best option at a node may change during the
    search. The algorithm stops when the start node is marked solved.
"""

# AND-OR graph: node -> list of options. Each option is a list of children.
#   One child in an option  -> OR choice (pick this option OR another one)
#   Several children        -> AND choice (ALL of them must be solved)
graph = {
    'A': [['B'], ['C', 'D']],   # A is solved via B, OR via (C AND D)
    'B': [['E', 'F']],          # B is solved via (E AND F)
    'C': [['G']],
    'D': [['H']],
    'E': [],                    # leaf nodes: no options
    'F': [],
    'G': [],
    'H': []
}

# h(n): estimate for non-leaf nodes, exact cost for leaf (primitive) nodes
heuristic = {
    'A': 3, 'B': 2, 'C': 1, 'D': 1,
    'E': 4, 'F': 3, 'G': 1, 'H': 2
}

EDGE_COST = 1  # every edge to a child costs 1


def ao_star(graph, heuristic, start):
    """
    Find the lowest-cost solution graph of an AND-OR graph using AO*.

    Parameters:
        graph (dict): AND-OR graph {node: [option, ...]}, option = [children].
        heuristic (dict): Estimated cost h(n) of every node.
        start (str): The root node of the problem.

    Returns:
        tuple: (solution, total_cost) where solution maps each node of the
        solution graph to its chosen option (list of children).
    """
    h = dict(heuristic)       # working cost estimates, revised as we go
    best = {}                 # node -> currently best option (list of children)
    expanded = set()          # nodes whose options have been evaluated
    solved = {node for node in graph if not graph[node]}  # leaves are solved

    def option_cost(option):
        # Cost of an option = sum of (edge cost + cost of each child)
        return sum(EDGE_COST + h[child] for child in option)

    def revise():
        # Re-evaluate every expanded node from the bottom up until stable
        changed = True
        while changed:
            changed = False
            for node in expanded:
                costs = [option_cost(option) for option in graph[node]]
                index = costs.index(min(costs))
                option = graph[node][index]
                is_solved = all(child in solved for child in option)

                if (h[node] != costs[index] or best.get(node) != option
                        or (node in solved) != is_solved):
                    h[node] = costs[index]
                    best[node] = option
                    if is_solved:
                        solved.add(node)
                    else:
                        solved.discard(node)
                    changed = True

    def find_unexpanded():
        # Walk down the current best solution graph to find a node to expand
        queue = [start]
        seen = set()
        while queue:
            node = queue.pop(0)
            if node in seen or node in solved:
                continue
            seen.add(node)
            if node not in expanded:
                return node
            queue.extend(best[node])
        return None

    # Main loop: expand and revise until the start node is solved
    while start not in solved:
        node = find_unexpanded()
        if node is None:
            break
        expanded.add(node)
        revise()

    # Collect the final solution graph by following the best options
    solution = {}
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node in best and node not in solution:
            solution[node] = best[node]
            queue.extend(best[node])

    return solution, h[start]


# Driver code
if __name__ == "__main__":
    solution, total_cost = ao_star(graph, heuristic, 'A')

    print("AO* Solution Graph:")
    for node, children in solution.items():
        print(node, "->", " AND ".join(children))
    print("Total Cost:", total_cost)

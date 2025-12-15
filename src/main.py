import os
from collections import deque

def main(argv):
    if len(argv) != 2:
        print("Usage: ./graph_solution path/to/graph.csv")
        return 1

    file_path = argv[1]
    if not os.path.isfile(file_path):
        print(f"Error: file not found: {file_path}")
        return 1

    edges = []
    nodes = set()

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            source, target = map(int, line.split(","))
            edges.append((source, target))
            nodes.add(source)
            nodes.add(target)

    if not nodes:
        print("is_dag: true")
        print("max_in_degree: 0")
        print("max_out_degree: 0")
        print("pr_max: 0.000000")
        print("pr_min: 0.000000")
        return 0

    adj_list = {node: [] for node in nodes}
    for source, target in edges:
        adj_list[source].append(target)

    in_degree = {node: 0 for node in nodes}
    out_degree = {node: 0 for node in nodes}

    for source, targets in adj_list.items():
        out_degree[source] = len(targets)
        for target in targets:
            in_degree[target] += 1

    max_in_degree = max(in_degree.values())
    max_out_degree = max(out_degree.values())

    in_degree_copy = dict(in_degree)
    queue = deque(node for node in in_degree_copy if in_degree_copy[node] == 0)

    processed_count = 0
    while queue:
        node = queue.popleft()
        processed_count += 1
        for neighbor in adj_list[node]:
            in_degree_copy[neighbor] -= 1
            if in_degree_copy[neighbor] == 0:
                queue.append(neighbor)

    is_dag = (processed_count == len(nodes))

    sorted_nodes = sorted(nodes)
    node_to_index = {node: idx for idx, node in enumerate(sorted_nodes)}

    n = len(nodes)
    pagerank = [1.0 / n for _ in range(n)]

    d = 0.85
    for _ in range(20):
        new_pagerank = [0.0] * n

        dangling_mass = sum(
            pagerank[node_to_index[node]]
            for node in nodes
            if out_degree[node] == 0
        )

        dangling_contribution = dangling_mass / n
        base_value = (1 - d) / n

        for i in range(n):
            new_pagerank[i] = base_value + d * dangling_contribution

    
        for source in sorted(adj_list):
            targets = adj_list[source]
            if not targets:
                continue

            src_idx = node_to_index[source]
            share = pagerank[src_idx] / len(targets)

            for target in sorted(targets):
                tgt_idx = node_to_index[target]
                new_pagerank[tgt_idx] += d * share

        pagerank = new_pagerank

    pr_max = round(max(pagerank), 6)
    pr_min = round(min(pagerank), 6)

    print(f"is_dag: {'true' if is_dag else 'false'}")
    print(f"max_in_degree: {max_in_degree}")
    print(f"max_out_degree: {max_out_degree}")
    print(f"pr_max: {pr_max:.6f}")
    print(f"pr_min: {pr_min:.6f}")

    return 0

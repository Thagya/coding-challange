# graph_solution — Graph Processing Assignment

## Summary
This repository contains a command-line program called `graph_solution` that:

1. Reads a directed graph from a CSV file
2. Computes:
   - `is_dag` (cycle detection)
   - `max_in_degree`
   - `max_out_degree`
   - `pr_max` (PageRank max)
   - `pr_min` (PageRank min)
3. Runs as:
   ./graph_solution path/to/graph.csv
4. Prints output in the exact required format (no extra text)

This solution is implemented in Python using only the standard library.



## Repository Contents
- `graph_solution` — executable entrypoint (no `.py` extension)
- `src/main.py` — implementation
- `requirements.txt` — dependency file (standard library only)
- `test_cases/` — example graphs and expected outputs (if included)


## Input Format
The CSV file must contain one directed edge per line:

source_node,target_node

Notes:
- No header
- Node IDs are treated as strings
- Empty lines are ignored

Example:
A,B
B,C
C,A



## Output Format
The program prints exactly 5 lines:

is_dag: true|false
max_in_degree: <int>
max_out_degree: <int>
pr_max: <float with 6 decimals>
pr_min: <float with 6 decimals>

Rules:
- `true`/`false` are lowercase
- PageRank values are printed with exactly 6 decimal places
- No additional output is printed



## Dependencies
No external packages are used.

See `requirements.txt` (intentionally empty except for comments).


## Running on *nix (Linux/macOS)
### 1) Ensure executable permission
From the repository root:

chmod +x graph_solution

### 2) Run
./graph_solution path/to/graph.csv

Example:
./graph_solution test_cases/graph1.csv



## How it Works (Implementation Notes)
### Graph Representation
- Adjacency list for outgoing edges
- In-degree and out-degree tracked for all nodes
- Nodes with no outgoing edges are included (empty adjacency list)

### DAG Detection
- Uses Kahn’s algorithm (topological removal)
- `is_dag` is true only if all nodes can be processed

### PageRank
- Damping factor: 0.85
- Exactly 20 iterations
- Handles dangling nodes (out-degree = 0) by redistributing their rank uniformly
- Implemented from scratch (no PageRank / graph libraries)






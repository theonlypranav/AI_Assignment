# Strategic Puzzle Agent – Tower of Hanoi

Artificial Intelligence Assignment
CS F407 – Artificial Intelligence
BITS Pilani

## Overview

This project implements a **Strategic Puzzle Agent** to solve the **Tower of Hanoi** problem using multiple search algorithms and heuristics.

The Tower of Hanoi consists of three pegs (**A, B, C**) and **n disks** initially stacked on peg **A** in decreasing size order.
The goal is to move all disks to peg **C** while obeying the following constraints:

1. Only one disk may be moved at a time.
2. A larger disk cannot be placed on top of a smaller disk.

The project demonstrates how different **search algorithms** explore the state space and how **heuristics** can guide the search efficiently.

---

## Implemented Algorithms

The following search algorithms are implemented from scratch (no external AI/search libraries used):

* **BFS** — Breadth-First Search
* **IDDFS** — Iterative Deepening Depth-First Search
* **Greedy** — Greedy Best-First Search
* **A\*** — A-Star Search
* **IDA\*** — Iterative Deepening A-Star

---

## Implemented Heuristics

Two admissible heuristics are used with the informed search algorithms:

### h₁ – Misplaced Disk Heuristic

Counts the number of disks not on the goal peg.

```
h1(s) = number of disks not on peg C
```

### h₂ – Largest Misplaced Disk Heuristic

Finds the largest disk (0-indexed) not yet placed on the goal peg and estimates cost based on the recursive structure of Hanoi.

```
k = index of the largest disk not on C  (0 = smallest disk)
h2(s) = 2^k − 1
```

This heuristic reflects the recursive nature of the Tower of Hanoi problem. Moving the k-th disk to the goal requires at least 2^k − 1 moves, making it a strong admissible lower bound.

---

## Project Structure

```
AI_Assignment/
│
├── main.py                  # main entry point — run a single algorithm
├── compare_algorithms.py    # compare all algorithms side by side
├── cases.py                 # predefined difficulty levels
├── readme.md
│
├── algorithms/
│   ├── __init__.py
│   ├── bfs.py               # Breadth-First Search
│   ├── iddfs.py              # Iterative Deepening DFS
│   ├── greedy.py             # Greedy Best-First Search
│   ├── astar.py              # A* Search
│   └── idastar.py            # IDA* Search
│
├── heuristics/
│   ├── __init__.py
│   ├── h1.py                 # misplaced disk count
│   └── h2.py                 # largest misplaced disk estimate
│
├── core/
│   ├── __init__.py
│   ├── state.py              # State representation
│   └── moves.py              # Move generation and application
│
└── visualization/
    ├── __init__.py
    └── visualizer.py         # step-by-step solution display
```

---

## Requirements

- Python 3.8 or higher
- No external libraries needed (only uses built-in modules: `heapq`, `collections`, `time`, `sys`)

---

## How to Run

Open a terminal inside the project directory.

### Single Algorithm Run

```
python main.py <algorithm> <heuristic> <disks_or_preset>
```

**Arguments:**
- `algorithm`: `bfs`, `iddfs`, `greedy`, `astar`, or `idastar`
- `heuristic`: `h1` or `h2` (used by greedy, astar, idastar; ignored by bfs/iddfs)
- `disks_or_preset`: a number (e.g. `3`) or a preset (`easy`, `medium`, `hard`)

### Compare All Algorithms

```
python compare_algorithms.py
```

You will be prompted to enter the number of disks. The script runs all algorithms and prints a comparison table.

---

## Example Runs

### BFS (3 disks)

```
python main.py bfs h1 3
```

### IDDFS (4 disks)

```
python main.py iddfs h1 4
```

### Greedy Best-First Search (5 disks)

```
python main.py greedy h2 5
```

### A* Search (5 disks)

```
python main.py astar h2 5
```

### IDA* Search (5 disks)

```
python main.py idastar h2 5
```

---

## Output

The program prints:

* Algorithm name, heuristic, and disk count
* Number of nodes expanded
* Execution time
* Number of moves in the solution
* Step-by-step visualization showing:
  - Move description (which disk, source → destination)
  - Peg contents at each step

Example output:

```
Algorithm: astar
Heuristic: h2
Disks: 3

Nodes Expanded: 10
Time: 0.001 seconds
Moves: 7

Solution Steps:

Solution found! (7 moves for 3 disks)

========================================
  Initial State
    Peg A: [1, 2, 3]
    Peg B: []
    Peg C: []
----------------------------------------
  Step 1: Move disk 1  A -> C
    Peg A: [2, 3]
    Peg B: []
    Peg C: [1]
----------------------------------------
  ...
```

---

## Algorithm Comparison (3 disks)

| Algorithm     | Nodes Expanded | Moves |
|---------------|---------------|-------|
| BFS           | ~26           | 7     |
| IDDFS         | ~30           | 7     |
| Greedy (h1)   | varies        | ≥ 7   |
| Greedy (h2)   | varies        | ≥ 7   |
| A* (h1)       | ~14           | 7     |
| A* (h2)       | ~10           | 7     |
| IDA* (h1)     | ~20           | 7     |
| IDA* (h2)     | ~12           | 7     |

> **Note:** Greedy search does not guarantee optimal solutions. BFS, IDDFS, A*, and IDA* all find the optimal 7-move solution for 3 disks.

---

## Visualization

The project includes a step-by-step visualization that prints the state of each peg after every move.
Each step shows:
- The move number and description (e.g., "Move disk 1  A -> C")
- The contents of all three pegs

This allows users to observe the progression of the search toward the goal state.

---

## Authors

Group 5 – Strategic Puzzle Agent

Harsh Nigam
Pranav Deshpande
Drishya Musaddi
Krishnansh Sood

CS F407 – Artificial Intelligence
BITS Pilani

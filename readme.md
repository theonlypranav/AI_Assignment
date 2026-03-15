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

# Implemented Algorithms

The following search algorithms are implemented from scratch:

* Breadth-First Search (**BFS**)
* Iterative Deepening Depth-First Search (**IDDFS**)
* Greedy Best-First Search
* A* Search

---

# Implemented Heuristics

Two admissible heuristics are used:

### h₁ – Misplaced Disk Heuristic

Counts the number of disks not on the goal peg.

```
h1(s) = number of disks not on peg C
```

### h₂ – Largest Incorrect Prefix Heuristic

Finds the largest disk not yet placed on the goal peg.

```
k = largest disk not on C
h2(s) = 2^k − 1
```

This heuristic reflects the recursive nature of the Tower of Hanoi problem and provides a stronger estimate than **h₁**.

---

# Project Structure

```
tower-hanoi-ai/
│
├── main.py
├── README.md
├── requirements.txt
│
├── algorithms/
│   ├── bfs.py
│   ├── iddfs.py
│   ├── greedy.py
│   └── astar.py
│
├── heuristics/
│   ├── h1.py
│   └── h2.py
│
├── core/
│   ├── state.py
│   └── moves.py
│
└── visualization/
    └── visualizer.py
```

---

# Requirements

Python 3.8 or higher

No external libraries are required.

---

# How to Run

Open a terminal inside the project directory.

General command format:

```
python main.py <algorithm> <heuristic> <number_of_disks>
```

---

# Example Runs

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

---

# Output

The program prints:

* Number of nodes expanded
* Execution time
* Number of moves
* Step-by-step visualization of peg configurations

Example output:

```
Nodes Expanded: 31
Time: 0.002
Moves: 31

A: [1,2,3]
B: []
C: []

-----
A: [2,3]
B: []
C: [1]
```

---

# Empirical Evaluation

The algorithms can be compared by running different configurations and observing:

* Nodes expanded
* Runtime
* Memory usage
* Solution depth

Example experiments:

| Disks | Algorithm | Nodes Expanded |
| ----- | --------- | -------------- |
| 3     | BFS       |                |
| 4     | BFS       |                |
| 5     | Greedy    |                |
| 5     | A*        |                |

These results are compared with theoretical complexity analysis.

---

# Visualization

The project includes a simple visualization that prints the state of each peg after every move.

Example:

```
A: [3,2]
B: []
C: [1]
```

This allows users to observe the progression of the search toward the goal state.

---

# Authors

Group 5 – Strategic Puzzle Agent

Harsh Nigam
Pranav Deshpande
Drishya Musaddi
Krishnansh Sood

CS F407 – Artificial Intelligence
BITS Pilani

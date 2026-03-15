# Strategic Puzzle Agent – Tower of Hanoi

Artificial Intelligence Assignment  
CS F407 – Artificial Intelligence  
BITS Pilani

---

## Overview

This project implements a **Strategic Puzzle Agent** to solve the **Tower of Hanoi** problem using multiple search algorithms and heuristics.

The Tower of Hanoi puzzle consists of three pegs (**A, B, C**) and **n disks** initially stacked on peg **A** in decreasing size order.

The goal is to move all disks to peg **C** while obeying the following constraints:

1. Only one disk may be moved at a time.
2. A larger disk cannot be placed on top of a smaller disk.

The project demonstrates how different **search algorithms** explore the state space and how **heuristics** guide the search efficiently.

---

# Implemented Algorithms

The following search algorithms are implemented from scratch:

- Breadth-First Search (**BFS**)
- Iterative Deepening Depth-First Search (**IDDFS**)
- Greedy Best-First Search
- **A\*** Search

---

# Implemented Heuristics

Two heuristics are implemented:

### h₁ – Misplaced Disk Heuristic

Counts the number of disks not on the goal peg.

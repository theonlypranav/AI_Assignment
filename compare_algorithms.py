import time

from core.state import State

from algorithms.bfs import bfs
from algorithms.iddfs import iddfs
from algorithms.greedy import greedy
from algorithms.astar import astar
from algorithms.idastar import idastar

from heuristics.h1 import h1
from heuristics.h2 import h2


def run_algorithm(name, func, start, heuristic=None):
    """Time a single algorithm run and return stats."""

    t0 = time.time()

    if heuristic is not None:
        goal, nodes = func(start, heuristic)
    else:
        goal, nodes = func(start)

    elapsed = round(time.time() - t0, 5)

    moves = goal.g if goal is not None else "N/A"

    return nodes, elapsed, moves


def compare(disks):
    """Run all algorithms on the same starting config and print a comparison table."""

    start = State(['A'] * disks)

    print(f"\n{'=' * 65}")
    print(f"  Tower of Hanoi — Algorithm Comparison ({disks} disks)")
    print(f"{'=' * 65}")

    header = f"{'Algorithm':<18}{'Nodes':<15}{'Time(s)':<12}{'Moves':<10}"
    print(header)
    print("-" * 65)

    configs = [
        ("BFS",           bfs,     None),
        ("IDDFS",         iddfs,   None),
        ("Greedy (h1)",   greedy,  h1),
        ("Greedy (h2)",   greedy,  h2),
        ("A* (h1)",       astar,   h1),
        ("A* (h2)",       astar,   h2),
        ("IDA* (h1)",     idastar, h1),
        ("IDA* (h2)",     idastar, h2),
    ]

    for label, func, h in configs:
        nodes, t, moves = run_algorithm(label, func, start, h)
        print(f"{label:<18}{nodes:<15}{t:<12}{moves}")

    print("-" * 65)


if __name__ == "__main__":
    try:
        n = int(input("Enter number of disks: "))
    except ValueError:
        print("Please enter a valid number.")
    else:
        compare(n)
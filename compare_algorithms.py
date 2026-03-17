import time

from algorithms import idastar
from core.state import State

from algorithms.bfs import bfs
from algorithms.iddfs import iddfs
from algorithms.greedy import greedy
from algorithms.astar import astar

from heuristics.h1 import h1
from heuristics.h2 import h2


def run_algorithm(name, func, start, heuristic=None):

    start_time = time.time()

    if heuristic:
        goal, nodes = func(start, heuristic)
    else:
        goal, nodes = func(start)

    end_time = time.time()

    # handle None safely
    if goal is None:
        moves = "NA"
    else:
        moves = goal.g

    return nodes, round(end_time - start_time, 5), moves


def compare(disks):

    start = State(['A'] * disks)

    print("\nTower of Hanoi Comparison")
    print("Disks:", disks)
    print("-" * 65)

    print(f"{'Algorithm':<15}{'Nodes Expanded':<18}{'Time(s)':<12}{'Moves':<10}")
    print("-" * 65)

    algorithms = [

        ("BFS", bfs, None),
        ("IDDFS", iddfs, None),
        ("Greedy(h2)", greedy, h2),
        ("A*(h2)", astar, h2)

    ]

    for name, func, heuristic in algorithms:

        nodes, t, moves = run_algorithm(name, func, start, heuristic)

        print(f"{name:<15}{nodes:<18}{t:<12}{moves}")


if __name__ == "__main__":

    disks = int(input("Enter number of disks: "))
    compare(disks)
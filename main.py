import sys
import time

from core.state import State
from cases import CASES

from algorithms.bfs import bfs
from algorithms.iddfs import iddfs
from algorithms.greedy import greedy
from algorithms.astar import astar
from algorithms.idastar import idastar

from heuristics.h1 import h1
from heuristics.h2 import h2

from visualization.visualizer import show_solution


def run():

    if len(sys.argv) < 4:
        print("Usage: python main.py <algorithm> <heuristic> <disks/easy/medium/hard>")
        return

    algorithm = sys.argv[1]
    heuristic = sys.argv[2]
    case = sys.argv[3]

    # determine number of disks
    if case in CASES:
        disks = CASES[case]
    else:
        disks = int(case)

    start = State(['A'] * disks)

    # choose heuristic
    if heuristic == "h1":
        h = h1
    else:
        h = h2

    start_time = time.time()

    # choose algorithm
    if algorithm == "bfs":
        goal, nodes = bfs(start)

    elif algorithm == "iddfs":
        goal, nodes = iddfs(start)

    elif algorithm == "greedy":
        goal, nodes = greedy(start, h)

    elif algorithm == "astar":
        goal, nodes = astar(start, h)

    elif algorithm == "idastar":
        goal, nodes = idastar(start, h)

    else:
        print("Unknown algorithm")
        return

    end_time = time.time()

    print("\nAlgorithm:", algorithm)
    print("Heuristic:", heuristic)
    print("Disks:", disks)

    print("\nNodes Expanded:", nodes)
    print("Time:", round(end_time - start_time, 5), "seconds")
    print("Moves:", goal.g)

    print("\nSolution Steps:\n")

    show_solution(goal)


if __name__ == "__main__":
    run()
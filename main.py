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
        print("  Algorithms: bfs, iddfs, greedy, astar, idastar")
        print("  Heuristics: h1, h2")
        return

    algo_name = sys.argv[1].lower()
    heur_name = sys.argv[2].lower()
    case_arg = sys.argv[3]

    # figure out number of disks
    if case_arg in CASES:
        num_disks = CASES[case_arg]
    else:
        try:
            num_disks = int(case_arg)
        except ValueError:
            print(f"Invalid case: {case_arg}")
            return

    initial = State(['A'] * num_disks)

    # pick heuristic
    if heur_name == "h1":
        h = h1
    elif heur_name == "h2":
        h = h2
    else:
        print(f"Unknown heuristic: {heur_name}")
        return

    t_start = time.time()

    # run the chosen algorithm
    if algo_name == "bfs":
        goal, nodes = bfs(initial)

    elif algo_name == "iddfs":
        goal, nodes = iddfs(initial)

    elif algo_name == "greedy":
        goal, nodes = greedy(initial, h)

    elif algo_name == "astar":
        goal, nodes = astar(initial, h)

    elif algo_name == "idastar":
        goal, nodes = idastar(initial, h)

    else:
        print(f"Unknown algorithm: {algo_name}")
        return

    elapsed = time.time() - t_start

    print(f"\nAlgorithm: {algo_name}")
    print(f"Heuristic: {heur_name}")
    print(f"Disks: {num_disks}")
    print(f"\nNodes Expanded: {nodes}")
    print(f"Time: {round(elapsed, 5)} seconds")

    if goal is not None:
        print(f"Moves: {goal.g}")
        print("\nSolution Steps:\n")
        show_solution(goal)
    else:
        print("No solution found.")


if __name__ == "__main__":
    run()
import sys
import time

from core.state import State

from algorithms.bfs import bfs
from algorithms.iddfs import iddfs
from algorithms.greedy import greedy
from algorithms.astar import astar

from heuristics.h1 import h1
from heuristics.h2 import h2

from visualization.visualizer import show_solution


def run():

    algorithm=sys.argv[1]
    heuristic=sys.argv[2]
    disks=int(sys.argv[3])

    start=State(['A']*disks)

    if heuristic=="h1":
        h=h1
    else:
        h=h2

    start_time=time.time()

    if algorithm=="bfs":
        goal,nodes=bfs(start)

    elif algorithm=="iddfs":
        goal,nodes=iddfs(start)

    elif algorithm=="greedy":
        goal,nodes=greedy(start,h)

    elif algorithm=="astar":
        goal,nodes=astar(start,h)

    else:
        print("Unknown algorithm")
        return

    end_time=time.time()

    print("\nNodes Expanded:",nodes)
    print("Time:",end_time-start_time)
    print("Moves:",goal.g)

    show_solution(goal)


if __name__=="__main__":
    run()
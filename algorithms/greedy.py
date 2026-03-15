import heapq
from core.moves import get_valid_moves, apply_move

def greedy(start, heuristic):

    frontier = []
    counter = 0

    heapq.heappush(frontier, (heuristic(start), counter, start))

    visited = set([start])
    nodes = 0

    while frontier:

        _, _, state = heapq.heappop(frontier)
        nodes += 1

        if state.is_goal():
            return state, nodes

        for move in get_valid_moves(state):

            child = apply_move(state, move)

            if child not in visited:

                visited.add(child)
                counter += 1
                heapq.heappush(frontier, (heuristic(child), counter, child))

    return None, nodes
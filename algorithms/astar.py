import heapq
from core.moves import get_valid_moves, apply_move

def astar(start, heuristic):

    frontier = []
    counter = 0

    heapq.heappush(frontier, (heuristic(start), 0, counter, start))

    visited = set([start])
    nodes = 0

    while frontier:

        f, g, _, state = heapq.heappop(frontier)
        nodes += 1

        if state.is_goal():
            return state, nodes

        for move in get_valid_moves(state):

            child = apply_move(state, move)

            if child not in visited:

                visited.add(child)

                g_new = g + 1
                f_new = g_new + heuristic(child)

                counter += 1

                heapq.heappush(frontier, (f_new, g_new, counter, child))

    return None, nodes
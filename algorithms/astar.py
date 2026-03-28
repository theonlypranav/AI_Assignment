import heapq
from core.moves import get_valid_moves, apply_move


def astar(start, heuristic):
    """A* search — uses f(n) = g(n) + h(n) to pick the next state."""

    open_list = []
    tie_breaker = 0

    h_val = heuristic(start)
    heapq.heappush(open_list, (h_val, 0, tie_breaker, start))

    # track best known g-cost for each state
    best_g = {start: 0}
    expanded = 0

    while open_list:
        f, g, _, state = heapq.heappop(open_list)

        # if we already found a cheaper way to this state, skip it
        if g > best_g.get(state, float('inf')):
            continue

        expanded += 1

        if state.is_goal():
            return state, expanded

        for move in get_valid_moves(state):
            child = apply_move(state, move)
            new_g = g + 1

            # only explore if this path is cheaper than any we've seen
            if new_g < best_g.get(child, float('inf')):
                best_g[child] = new_g
                f_val = new_g + heuristic(child)
                tie_breaker += 1
                heapq.heappush(open_list, (f_val, new_g, tie_breaker, child))

    return None, expanded
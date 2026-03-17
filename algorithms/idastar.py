from core.moves import get_valid_moves, apply_move


def ida_search(state, g, bound, heuristic, path, nodes):

    nodes[0] += 1

    f = g + heuristic(state)

    if f > bound:
        return f, None

    if state.is_goal():
        return f, state

    minimum = float("inf")

    path.add(state)

    for move in get_valid_moves(state):

        child = apply_move(state, move)

        if child not in path:

            temp, result = ida_search(child, g + 1, bound, heuristic, path, nodes)

            if result is not None:
                return temp, result

            if temp < minimum:
                minimum = temp

    path.remove(state)

    return minimum, None


def idastar(start, heuristic):

    bound = heuristic(start)
    nodes = [0]

    while True:

        path = set()

        temp, result = ida_search(start, 0, bound, heuristic, path, nodes)

        if result is not None:
            return result, nodes[0]

        if temp == float("inf"):
            return None, nodes[0]

        bound = temp
from core.moves import get_valid_moves, apply_move


def dls(state, depth, nodes):

    nodes[0] += 1

    if state.is_goal():
        return state

    if depth <= 0:
        return None

    for move in get_valid_moves(state):

        child = apply_move(state, move)

        result = dls(child, depth - 1, nodes)

        if result:
            return result

    return None


def iddfs(start, max_depth=100000):

    for depth in range(1, max_depth + 1):

        nodes = [0]

        result = dls(start, depth, nodes)

        if result is not None:
            return result, nodes[0]

    return None, nodes[0]
from core.moves import get_valid_moves, apply_move

def dls(state, depth, visited):

    if state.is_goal():
        return state

    if depth == 0:
        return None

    visited.add(state)

    for move in get_valid_moves(state):

        child = apply_move(state, move)

        if child not in visited:

            result = dls(child, depth-1, visited)

            if result:
                return result

    return None


def iddfs(start, max_depth=50):

    for depth in range(max_depth):

        visited = set()

        result = dls(start, depth, visited)

        if result:
            return result, len(visited)

    return None, 0
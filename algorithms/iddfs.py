from core.moves import get_valid_moves, apply_move


def depth_limited_search(state, limit, visited_path, node_count):
    """Run DFS up to a given depth limit, tracking path to avoid cycles."""

    node_count[0] += 1

    if state.is_goal():
        return state

    if limit <= 0:
        return None

    visited_path.add(state)

    for move in get_valid_moves(state):
        child = apply_move(state, move)

        # skip states already on the current path (cycle avoidance)
        if child in visited_path:
            continue

        result = depth_limited_search(child, limit - 1, visited_path, node_count)
        if result is not None:
            return result

    visited_path.discard(state)
    return None


def iddfs(start, max_depth=100):
    """Iterative deepening — runs depth-limited search at increasing depths."""

    total_nodes = [0]

    for depth in range(1, max_depth + 1):
        path_set = set()
        result = depth_limited_search(start, depth, path_set, total_nodes)

        if result is not None:
            return result, total_nodes[0]

    return None, total_nodes[0]
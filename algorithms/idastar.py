from core.moves import get_valid_moves, apply_move


def _search(state, g, threshold, heuristic, current_path, counter):
    """Recursive helper for IDA* — returns (next_threshold, goal_state_or_None)."""

    counter[0] += 1
    f = g + heuristic(state)

    if f > threshold:
        return f, None

    if state.is_goal():
        return f, state

    next_threshold = float("inf")
    current_path.add(state)

    for move in get_valid_moves(state):
        child = apply_move(state, move)

        if child in current_path:
            continue

        t, found = _search(child, g + 1, threshold, heuristic, current_path, counter)

        if found is not None:
            return t, found

        if t < next_threshold:
            next_threshold = t

    current_path.discard(state)
    return next_threshold, None


def idastar(start, heuristic):
    """IDA* — iterative deepening version of A*, uses less memory."""

    threshold = heuristic(start)
    total_nodes = [0]

    while True:
        path = set()
        t, goal = _search(start, 0, threshold, heuristic, path, total_nodes)

        if goal is not None:
            return goal, total_nodes[0]

        # no more states to explore
        if t == float("inf"):
            return None, total_nodes[0]

        threshold = t
from collections import deque
from core.moves import get_valid_moves, apply_move


def bfs(start):
    """Breadth-first search — guarantees shortest path (fewest moves)."""

    queue = deque()
    queue.append(start)
    explored = {start}

    nodes_checked = 0

    while queue:
        current = queue.popleft()
        nodes_checked += 1

        if current.is_goal():
            return current, nodes_checked

        for move in get_valid_moves(current):
            neighbor = apply_move(current, move)

            if neighbor not in explored:
                explored.add(neighbor)
                queue.append(neighbor)

    # no solution found
    return None, nodes_checked
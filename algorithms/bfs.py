from collections import deque
from core.moves import get_valid_moves, apply_move

def bfs(start):

    frontier = deque([start])
    visited = set([start])

    nodes = 0

    while frontier:

        state = frontier.popleft()
        nodes += 1

        if state.is_goal():
            return state, nodes

        for move in get_valid_moves(state):

            child = apply_move(state, move)

            if child not in visited:
                visited.add(child)
                frontier.append(child)

    return None, nodes
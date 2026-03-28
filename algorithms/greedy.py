import heapq
from core.moves import get_valid_moves, apply_move


def greedy(start, heuristic):
    """
    Greedy best-first search — expands the node with lowest h(n).
    NOTE: this does NOT guarantee an optimal solution since it ignores path cost.
    """

    pq = []
    seq = 0  # tie-breaking counter

    heapq.heappush(pq, (heuristic(start), seq, start))

    seen = set()
    seen.add(start)
    expansions = 0

    while pq:
        h_val, _, node = heapq.heappop(pq)
        expansions += 1

        if node.is_goal():
            return node, expansions

        for move in get_valid_moves(node):
            child = apply_move(node, move)

            if child not in seen:
                seen.add(child)
                seq += 1
                heapq.heappush(pq, (heuristic(child), seq, child))

    return None, expansions
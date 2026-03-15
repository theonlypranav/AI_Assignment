from core.state import State

def get_valid_moves(state):

    pegs = {'A': [], 'B': [], 'C': []}

    for i, peg in enumerate(state.pegs):
        pegs[peg].append(i)

    for p in pegs:
        pegs[p].sort()

    moves = []

    for src in ['A','B','C']:

        if not pegs[src]:
            continue

        disk = min(pegs[src])

        for dest in ['A','B','C']:

            if src == dest:
                continue

            if not pegs[dest] or disk < min(pegs[dest]):
                moves.append((disk, src, dest))

    return moves


def apply_move(state, move):

    disk, src, dest = move

    new_pegs = list(state.pegs)
    new_pegs[disk] = dest

    return State(new_pegs, state, move, state.g + 1)
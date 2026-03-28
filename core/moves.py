from core.state import State


def get_valid_moves(state):
    """
    Figure out which moves are legal from the current state.
    Returns a list of (disk_index, source_peg, destination_peg) tuples.
    """

    # group disks by which peg they're on
    peg_contents = {'A': [], 'B': [], 'C': []}

    for disk, peg in enumerate(state.pegs):
        peg_contents[peg].append(disk)

    # sort so smallest disk index is first on each peg
    for p in peg_contents:
        peg_contents[p].sort()

    result = []

    for src in ['A', 'B', 'C']:
        if len(peg_contents[src]) == 0:
            continue

        # only the top disk (smallest index) can move
        top_disk = peg_contents[src][0]

        for dst in ['A', 'B', 'C']:
            if src == dst:
                continue

            # can only place on empty peg or on top of a larger disk
            if len(peg_contents[dst]) == 0 or top_disk < peg_contents[dst][0]:
                this_move = (top_disk, src, dst)

                # don't just undo the last move
                if state.move and (top_disk, dst, src) == state.move:
                    continue

                result.append(this_move)

    return result


def apply_move(state, move):
    """Apply a move and return the resulting new state."""
    disk, src, dst = move

    new_pegs = list(state.pegs)
    new_pegs[disk] = dst

    return State(new_pegs, parent=state, move=move, g=state.g + 1)
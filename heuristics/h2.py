def h2(state):
    # find the largest disk (0-indexed) that hasn't reached peg C yet
    largest_misplaced = -1

    for disk_idx, peg in enumerate(state.pegs):
        if peg != 'C':
            largest_misplaced = disk_idx

    if largest_misplaced < 0:
        return 0

    # minimum moves needed to get disk k (and everything above it) to goal
    return (2 ** largest_misplaced) - 1
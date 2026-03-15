def h2(state):

    k = 0

    for i, peg in enumerate(state.pegs, start=1):
        if peg != 'C':
            k = i

    if k == 0:
        return 0

    return (2 ** k) - 1
def h1(state):
    # simply count how many disks are not on the goal peg
    count = 0
    for p in state.pegs:
        if p != 'C':
            count += 1
    return count
def h1(state):
    return sum(1 for p in state.pegs if p != 'C')
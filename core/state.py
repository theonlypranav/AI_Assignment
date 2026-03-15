class State:

    def __init__(self, pegs, parent=None, move=None, g=0):
        self.pegs = tuple(pegs)     # immutable for hashing
        self.parent = parent
        self.move = move
        self.g = g                  # path cost (number of moves)

    def is_goal(self):
        return all(p == 'C' for p in self.pegs)

    def __hash__(self):
        return hash(self.pegs)

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.pegs == other.pegs

    def __repr__(self):
        return f"State({self.pegs})"
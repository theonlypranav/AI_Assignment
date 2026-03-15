class State:

    def __init__(self, pegs, parent=None, move=None, g=0):
        self.pegs = tuple(pegs)
        self.parent = parent
        self.move = move
        self.g = g

    def is_goal(self):
        return all(p == 'C' for p in self.pegs)

    def __hash__(self):
        return hash(self.pegs)

    def __eq__(self, other):
        return self.pegs == other.pegs
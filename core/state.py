class State:
    """Represents one configuration of the Tower of Hanoi puzzle."""

    def __init__(self, pegs, parent=None, move=None, g=0):
        self.pegs = tuple(pegs)     # make it immutable so we can hash it
        self.parent = parent
        self.move = move            # the move that led to this state
        self.g = g                  # cost so far (number of moves taken)

    def is_goal(self):
        """Check if every disk is on peg C."""
        for p in self.pegs:
            if p != 'C':
                return False
        return True

    def __hash__(self):
        return hash(self.pegs)

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.pegs == other.pegs

    def __lt__(self, other):
        # needed so heapq doesn't crash when two states have the same priority
        return self.pegs < other.pegs

    def __repr__(self):
        return f"State({self.pegs})"
import time


def show_solution(goal):
    """Walk back from goal state to start, then print each step with move info."""

    if goal is None:
        print("No solution was found.")
        return

    # trace the path from goal back to start
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = node.parent
    path.reverse()

    num_disks = len(path[0].pegs)
    print(f"Solution found! ({len(path) - 1} moves for {num_disks} disks)\n")
    print("=" * 40)

    for step, state in enumerate(path):

        # build the peg lists for display
        peg_a = []
        peg_b = []
        peg_c = []

        for disk, peg in enumerate(state.pegs):
            disk_label = disk + 1  # show 1-indexed to the user
            if peg == 'A':
                peg_a.append(disk_label)
            elif peg == 'B':
                peg_b.append(disk_label)
            else:
                peg_c.append(disk_label)

        if step == 0:
            print(f"  Initial State")
        else:
            mv = state.move
            disk_num = mv[0] + 1  # 1-indexed for display
            print(f"  Step {step}: Move disk {disk_num}  {mv[1]} -> {mv[2]}")

        print(f"    Peg A: {peg_a}")
        print(f"    Peg B: {peg_b}")
        print(f"    Peg C: {peg_c}")
        print("-" * 40)

        time.sleep(0.3)

    print(f"\nDone — total moves: {len(path) - 1}")
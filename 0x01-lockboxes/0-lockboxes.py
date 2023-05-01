"""Solving the Lockboxes Problem """


def canUnlockAll(boxes)
    """
    A Method that Takes only List of List
    Returns bool
    Checks whether all boxes are unlockable
    """
    unlocked = {0}
    keys = set(boxes[0])

    while keys:
        box = keys.pop()
        if box not in unlocked:
            unlocked.add(box)
            keys.update(boxes[box])

    return len(unlocked) == len(boxes)

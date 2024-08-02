#!/usr/bin/python3
""""
A module that provedies a function that determines
if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """A function that determines if all the boxes can be opened."""
    n = len(boxes)
    openedBoxes = set([0])
    lockedBoxes = set([0])
    while len(lockedBoxes) > 0:
        box = lockedBoxes.pop()
        for k in boxes[box]:
            if k < n and k not in openedBoxes:
                openedBoxes.add(k)
                lockedBoxes.add(k)
    return n == len(openedBoxes)

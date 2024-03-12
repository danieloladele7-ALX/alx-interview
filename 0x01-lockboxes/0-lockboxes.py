#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for key in range(1, len(boxes) - 1):
        box_state = False
        for idx in range(len(boxes)):
            box_state = (key in boxes[idx] and key != idx)
            if box_state:
                break
        if box_state is False:
            return box_state
    return True

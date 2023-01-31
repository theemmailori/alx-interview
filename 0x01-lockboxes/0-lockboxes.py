#!/usr/bin/python3
"""
Contains a function called canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    keys = []
    for box in boxes:
        try:
            keys.append(box[0])
        except IndexError:
            pass
    for required_key in range(1, len(boxes)):
        if required_key not in keys:
            return False
    return True

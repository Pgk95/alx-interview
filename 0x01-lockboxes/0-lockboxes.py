#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """returns (True) if all boxes can be opened
    else return (False)"""
    if type(boxes) != list:
        return False

    lengthOfBoxes = len(boxes)
    boxestoOpen = [0]
    openedBoxes = set()

    while boxestoOpen:
        boxIndex = boxestoOpen.pop()
        openedBoxes.add(boxIndex)

        if type(boxes[boxIndex]) != list:
            return False

        for key in boxes[boxIndex]:
            if (key < lengthOfBoxes) and (key not in boxestoOpen) and\
                    (key not in openedBoxes):
                boxestoOpen.append(key)

    return len(openedBoxes) == len(boxes)

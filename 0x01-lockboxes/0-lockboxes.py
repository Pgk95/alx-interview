#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """returns (True) if all boxes can be opened
    else return (False)"""

    if type(boxes) != list:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        if type(boxes[current_box]) != list:
            return False

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                stack.append(key)
    return all(visited)

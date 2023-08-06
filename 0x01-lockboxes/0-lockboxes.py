#!/usr/bin/env python3
'''Function to check unlocked boxes'''


def canUnlockAll(boxes, visited=None, current_box=0):
    '''Unlock a box'''
    if visited is None:
        visited = set()

    if current_box in visited:
        return False

    visited.add(current_box)

    if len(visited) == len(boxes):
        return True

    for key in boxes[current_box]:
        if canUnlockAll(boxes, visited, key):
            return True

    return False

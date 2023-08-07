#!/usr/bin/python3
'''Function to check unlocked boxes'''


def canUnlockAll(boxes):
    '''unlock boxes'''
    visited = set()
    visited.add(0)
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)

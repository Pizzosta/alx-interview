#!/usr/bin/python3
'''Pascals Triangle'''


def pascal_triangle(n):
    if n == 0:
        return []

    triangle = [[1]]
    for i in range(2, n + 1):
        row = [None] * i
        row[0], row[-1] = 1, 1

        for j in range(1, i - 1):
            row[j] = triangle[-1][j - 1] + triangle[-1][j]

        triangle.append(row)

    return triangle

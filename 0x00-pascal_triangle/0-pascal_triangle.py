#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row in range(2, n + 1):
        rows = []

        for idx in range(row):
            if idx == 0 or idx == row - 1:
                rows.append(1)
                continue
            value = triangle[row - 2][idx] + triangle[row - 2][idx - 1]
            rows.append(value)

        triangle.append(rows)

    return triangle

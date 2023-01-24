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

    result_list = []
    result_list.append([1])

    for row in range(2, n + 1):
        row_list = []
        for idx in range(row):
            if idx == 0:
                row_list.append(1)
                continue
            if idx == row - 1:
                row_list.append(1)
                break
            element = result_list[row - 2][idx] + result_list[row - 2][idx - 1]
            row_list.append(element)

        result_list.append(row_list)

    return result_list

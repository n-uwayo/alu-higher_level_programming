#!/usr/bin/python3
"""
This module defines a function for multiplying two matrices.
"""

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Return:
        new matrix representing the multiplication of m_a by m_b.
    Raises:
        ValueError: if m_a or m_b is not a matrix, or if m_a and m_b cannot be multiplied.
    """

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise ValueError("m_a must be a matrix")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("m_b must be a matrix")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

if __name__ == '__main__':
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    # Expected output: [[7, 10], [15, 22]]
    print(matrix_mul([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]]))
    # Expected output: [[22, 28], [49, 64]]
    try:
        print(matrix_mul([[1, 2], [3, 4, 1]], [[1, 2, 3], [3, 4]]))
        # Expected output: ValueError: m_a must be a matrix
    except ValueError as e:
        print(str(e))  # Expected output: m_a must be a matrix

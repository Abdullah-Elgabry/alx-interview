#!/usr/bin/python3
"""Module to rotate a 2D matrix 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """Rotates a given `n x n` 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list): A list of [] representing the matrix to rotate.
    The function modifies the matrix in place, without using additional
    memory for another 2D matrix.
    """
    # Make a shallow copy of the matrix to use as a reference
    replica = matrix[:]

    for i in range(len(matrix)):
        # Extracts the column from the replica to form a new row
        column = [row[i] for row in replica]
        # Replaces the row in the matrix with the reversed column
        matrix[i] = column[::-1]

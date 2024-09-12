#!/usr/bin/python3
"""
Integration test for the `rotate_2d_matrix` function.
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    # Sample 3x3 matrix to test the rotation
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    # Rotates the 2D matrix in-place by 90 degrees
    rotate_2d_matrix(matrix)

    # Prints the rotated matrix to verify correctness
    print(matrix)

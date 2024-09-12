Rotate 2D Matrix

## Description

This project contains a Python function to rotate a given 2D matrix 90 degrees clockwise. The function takes a square matrix (n x n) and modifies it in place to produce the rotated output. Additionally, the project includes tests to verify the correctness of the rotation function.

## Files

- **0-rotate_2d_matrix.py**: Contains the implementation of the `rotate_2d_matrix` function.
- **test_rotate_2d_matrix.py**: An integration test script to validate the rotation function.
- **app.py**: A simple Flask app with user authentication features.
- **auth.py**: Contains authentication-related routines for managing user accounts.
- **db.py**: Database management module for handling user data and sessions.
- **user.py**: Defines the user model using SQLAlchemy ORM.
- **e2e_test.py**: End-to-end integration test for `app.py`.

## Function Overview

### `rotate_2d_matrix(matrix)`

- **Args**:
  - `matrix (list of lists)`: A 2D list representing an n x n matrix.
- **Description**: Rotates the given matrix 90 degrees clockwise, modifying it in place.
- **Example**:

  ```python
  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]
  rotate_2d_matrix(matrix)
  print(matrix)
  # Output:
  # [
  #     [7, 4, 1],
  #     [8, 5, 2],
  #     [9, 6, 3]
  # ]
  ```

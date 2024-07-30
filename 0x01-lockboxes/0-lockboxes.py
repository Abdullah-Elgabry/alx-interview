#!/usr/bin/python3
"""Solves the lock boxes puzzle."""


def get_keys_from_next_unchecked_box(unchecked_boxes):
    """
    Retrieves the keys from the next box that has been opened

    Args:
        unchecked_boxes (dict): {} containing info about unchecked boxes.

    Returns:
        list: List of keys found in the opened but unchecked box.
    """
    for index, box in unchecked_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'checked'
            return box.get('keys')
    return None


def all_boxes_can_be_unlocked(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): List containing all the boxes with their respective keys.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    b = {}
    while True:
        if len(b) == 0:
            b[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = get_keys_from_next_unchecked_box(b)
        if keys:
            for key in keys:
                try:
                    if b.get(key) and b.get(key).get('status') == 'checked':
                        continue
                    b[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in b.values()]:
            continue
        elif len(b) == len(boxes):
            break
        else:
            return False

    return len(b) == len(boxes)


def main():
    """Main entry point for testing the all_boxes_can_be_unlocked function."""
    print(all_boxes_can_be_unlocked([[]]))  # Example test


if __name__ == '__main__':
    main()

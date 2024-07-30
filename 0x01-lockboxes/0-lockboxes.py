#!/usr/bin/python3
"""Solves the lock boxes puzzle."""


def get_keys_from_next_unchecked_box(unchecked_boxes):
    """
    Retrieves the keys from the next box that has been opened but not yet checked.
    
    Args:
        unchecked_boxes (dict): Dictionary containing information about unchecked boxes.
    
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

    unlock_box = {}
    while True:
        if len(unlock_box) == 0:
            unlock_box[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = get_keys_from_next_unchecked_box(unlock_box)
        if keys:
            for key in keys:
                try:
                    if unlock_box.get(key) and unlock_box.get(key).get('status') == 'checked':
                        continue
                    unlock_box[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in unlock_box.values()]:
            continue
        elif len(unlock_box) == len(boxes):
            break
        else:
            return False

    return len(unlock_box) == len(boxes)


def main():
    """Main entry point for testing the all_boxes_can_be_unlocked function."""
    print(all_boxes_can_be_unlocked([[]]))  # Example test


if __name__ == '__main__':
    main()

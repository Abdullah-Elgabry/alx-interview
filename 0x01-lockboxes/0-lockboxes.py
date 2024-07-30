#!/usr/bin/python3
""" lock boxes task """


def find_next_open_box(open_boxes):
    """searching for the coming box.

    Args:
        open_boxes (dict): {} brev openned boxes

    Returns:
        list: [] openned boxes keys
    """
    for index, box in open_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """ckecking function of oppend boxes

    Args:
        boxes (list): [] have * box with the keys.

    Returns:
        bool: false in case canot open otherwise True.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    checker = {}
    while True:
        if len(checker) == 0:
            checker[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = find_next_open_box(checker)
        if keys:
            for tgt in keys:
                try:
                    if checker.get(tgt) and checker.get(tgt).get('status') \
                       == 'opened/checked':
                        continue
                    checker[tgt] = {
                        'status': 'opened',
                        'keys': boxes[tgt]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in checker.values()]:
            continue
        elif len(checker) == len(boxes):
            break
        else:
            return False

    return len(checker) == len(boxes)


def entry_point():
    """testing canUnlockAll (main function)"""
    canUnlockAll([[]])  # test


if __name__ == '__main__':
    entry_point()

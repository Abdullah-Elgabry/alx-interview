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


def openastrc(all_boxes):
    """ckecking function of oppend boxes

    Args:
        all_boxes (list): [] have * box with the keys.

    Returns:
        bool: false in case canot open otherwise True.
    """
    if len(all_boxes) <= 1 or all_boxes == [[]]:
        return True

    checker = {}
    while True:
        if len(checker) == 0:
            checker[0] = {
                'status': 'opened',
                'keys': all_boxes[0],
            }
        keys = find_next_open_box(checker)
        if keys:
            for key in keys:
                try:
                    if checker.get(key) and checker.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    checker[key] = {
                        'status': 'opened',
                        'keys': all_boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in checker.values()]:
            continue
        elif len(checker) == len(all_boxes):
            break
        else:
            return False

    return len(checker) == len(all_boxes)


def entry_point():
    """testing"""
    openastrc([[]])  # test


if __name__ == '__main__':
    entry_point()

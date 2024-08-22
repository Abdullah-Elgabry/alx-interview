#!/usr/bin/python3
""" Task 0x04 module"""


def validUTF8(data):
    """
    This function will checks if data is writen in UTF-8 encoding or not.
    """
    siz_loc = 0

    fst = 1 << 7
    nd = 1 << 6

    for x in data:

        chk_loc = 1 << 7

        if siz_loc == 0:

            while chk_loc & x:
                siz_loc += 1
                chk_loc = chk_loc >> 1

            if siz_loc == 0:
                continue

            if siz_loc == 1 or siz_loc > 4:
                return False

        else:
            if not (x & fst and not (x & nd)):
                    return False

        siz_loc -= 1

    if siz_loc == 0:
        return True

    return False

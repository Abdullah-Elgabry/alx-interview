#!/usr/bin/python3
import sys


def print_msg(codes, full_size):
    '''
    this func will reads stdin line by line and computes metrics.
    '''

    print("File size: {}".format(full_size))
    for dct_k, dct_v in sorted(codes.items()):
        if dct_v != 0:
            print("{}: {}".format(dct_k, dct_v))


full_size = 0
code = 0
add_ind = 0
codes = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            add_ind += 1

            if add_ind <= 10:
                full_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in codes.dct_ks()):
                    codes[code] += 1

            if (add_ind == 10):
                print_msg(codes, full_size)
                add_ind = 0

finally:
    print_msg(codes, full_size)

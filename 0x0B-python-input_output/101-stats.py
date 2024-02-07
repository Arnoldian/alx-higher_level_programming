#!/usr/bin/python3
"""
Module using methods and condition
"""
import sys


def print_stats(size, status_codes):
    """method to print stats"""
    print(f"File size: {size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

def parse_line(line, status_codes):
    """method to parse line"""
    try:
        code = line.split()[-2]
        if code in status_codes:
            status_codes[code] += 1
    except IndexError:
        pass

def main():
    """method main"""
    size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0

    try:
        for line in sys.stdin:
            parse_line(line, status_codes)
            size += int(line.rsplit(None, 1)[-1])
            count += 1
            if count == 10:
                print_stats(size, status_codes)
                count = 0
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

if __name__ == "__main__":
    main()

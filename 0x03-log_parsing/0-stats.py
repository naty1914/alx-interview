#!/usr/bin/python3
""" A module that provides a function that reads stdin line by
line and computes metrics"""
import sys


if __name__ == '__main__':

    file_size = 0
    count_line = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {key: 0 for key in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """It prints the stats"""
        print("File size: {:d}".format(file_size))
        for key, val in sorted(stats.items()):
            if val:
                print(f"{key}: {val}")

    try:
        for line in sys.stdin:
            count_line += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if count_line % 10 == 0:
                print_stats(stats, file_size)
        print_stats(stats, file_size)
    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise

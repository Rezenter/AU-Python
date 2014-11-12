__author__ = 'rezenter'
import sys


def result(c):
    if c == 2:
        return 1
    if c == 1:
        return 0
    if c == 0:
        return 0
    return result(c-1)+result(c-2)+result(c-3)


if __name__ == '__main__':
    args = sys.argv
    n = int(args[1])
    i = 0
    while i <= n:
        print(result(i), end=' ')
        i += 1
    print()
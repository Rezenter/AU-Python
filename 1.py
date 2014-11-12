__author__ = 'rezenter'
import functional as f
import sys


def main():

    b = sys.argv[1:]
    a = []
    for i in b:
        a.append(int(i))
    print(f.myreduce(lambda x, y: x + y, a) + a[0])
if __name__ == '__main__':
    main()

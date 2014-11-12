__author__ = 'rezenter'
import functional
import sys


def main():

    b = sys.argv[1:]
    a = []
    for i in b:
        a.append(int(i))
    print(functional.myreduce())
if __name__ == '__main__':
    main()
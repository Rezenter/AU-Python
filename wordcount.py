__author__ = 'rezenter'


import sys


def lowercase(text):
        

def print_words(filename):
    file = open(filename[2:], 'r')
    clone = file.readlines()
    file.close()
    lowercase(clone)
    words = []
    count = []
    i = 0
    while len(clone) != 0:
        i += i
        word = clone[0][0]
        words.append(word)
        count[i] += count[i]


def print_top(filename):
    print(0)


def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()
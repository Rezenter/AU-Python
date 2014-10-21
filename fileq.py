__author__ = 'rezenter'
import fileqlib
import sys

if __name__ == '__main__':
    args = sys.argv
    if args[1] == '--equals':
        print(fileqlib.files_equal(args[2], args[3]))
    elif args[1] == '--eqsearch':
        print(fileqlib.find_eq_files(args[2], args[3]))
    else:
        print('for science... you monster.')
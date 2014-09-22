__author__ = 'rezenter'

import sys
def reverser(path_in, path_out):
    file_in = open(path_in + 'in.txt', 'r')
    result = ''
    for line in file_in:
        tmp = ''
        current_line = line
        length = len(current_line)
        if current_line.find('\n') != -1:
            for counter in range(0, length-1):
                tmp += current_line[length-counter-2]
            tmp += '\n'
        else:
            for counter in range(0, length):
                tmp += current_line[length-counter-1]
        result += tmp
    file_in.close()
    file_out = open(path_out + 'out.txt', 'w')
    file_out.write(result)
    print(result)
args = sys.argv
if args[1].find('if') != -1 and args[3].find('of') != -1:
    path_in = args[2]
    path_out = args[4]
    reverser(path_in, path_out)
elif args[3].find('if') != -1 and args[1].find('of') != -1:
    path_in = args[4]
    path_out = args[2]
    reverser(path_in, path_out)
else:
    print('For science you monster')
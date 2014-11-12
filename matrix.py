__author__ = 'rezenter'
matrix = []


def height():
    return len(matrix)


def length():
    return len(matrix[0])


def get_matrix():
    result = ''
    for i in range(0, height() - 1):
        for a in range(0, length() - 1):
            result += '%10d' % matrix[i][a] + ' '
            a += 1
        i += 1
        result += '\n'
    return result


def append_line(n):
    matrix.append(n)
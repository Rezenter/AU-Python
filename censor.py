__author__ = 'rezenter'

import sys
import string


def stars(n):
    res = ''
    while n > 0:
        res += '*'
        n -= 1
    return res


def result(path1, path2):
    text_file = open(path2, 'r')
    text = str(text_file.readlines()).lower()
    text_file.close()
    bad_file = open(path1, 'r')
    bad_list = bad_file.readlines()
    for i in range(0, len(bad_list)):
        bad_list[i] = bad_list[i][0: len(bad_list[i]) - 1]
        index = text.find(bad_list[i])
        if string.ascii_lowercase.find(text[index - 1]) == -1 or string.ascii_lowercase.find(text[index + len(bad_list[i])]) == -1:
            index = -1
        while index != -1:
            text = text[0: index] + ' ' + str(stars(len(bad_list[i])) + text[index + len(bad_list[i])+1: len(text) - 1])
            index = text.find(bad_list[i])
            if string.ascii_lowercase.find(text[index - 1]) == -1 or string.ascii_lowercase.find(text[index + len(bad_list[i])]) == -1:
                index = -1
    return text


if __name__ == '__main__':
    args = sys.argv
    bad_path = args[1]
    text_path = args[2]
    print(result(bad_path, text_path))


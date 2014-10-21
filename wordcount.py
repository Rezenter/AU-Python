__author__ = 'rezenter'


import sys


def lowercase(text):
    text_length = len(text)
    i = 0
    while i < text_length:
        tmp_string = ''
        a = 0
        string_length = len(text[i])
        while a < string_length:
            if 64 <= ord(text[i][a]) < 91:
                tmp_string += chr(ord(text[i][a]) + 32)
            elif 1040 <= ord(text[i][a]) < 1071:
                tmp_string += chr(ord(text[i][a]) + 32)
            else:
                tmp_string += text[i][a]
            a += 1
        text[i] = tmp_string
        i += 1
    return text


def addition(string, begin, end, words_dictionary):
    word = string[begin: end]
    if words_dictionary.get(word, -1) == -1:
        words_dictionary.update({word: 1})
    else:
        words_dictionary[word] += 1
    return words_dictionary


def dictionary(text):
    words_dictionary = {}
    text_length = len(text)
    i = 0

    while i < text_length:
        begin = -1
        end = -1
        a = 0
        string_length = len(text[i])
        print(text[i].split())
        while a < string_length:
            if 97 <= ord(text[i][a]) < 123 or 1072 <= ord(text[i][a]) < 1104:
                if begin == -1:
                    begin = a
                if a == string_length - 1:
                    end = a + 1
                    words_dictionary = addition(text[i], begin, end, words_dictionary)
                    begin = -1
                    end = -1

            else:
                if end == -1 and begin != -1:
                    end = a
                    words_dictionary = addition(text[i], begin, end, words_dictionary)
                    begin = -1
                    end = -1
            a += 1
        i += 1
    return words_dictionary


def count(local_dictionary):
    return local_dictionary[1]


def print_words(filename):
    file = open(filename, 'r')
    clone = lowercase(file.readlines())
    file.close()
    print(list(sorted(dictionary(clone).items(), key=count, reverse=1)))


def print_top(filename):
    file = open(filename, 'r')
    clone = lowercase(file.readlines())
    file.close()
    out = list(sorted(dictionary(clone).items(), key=count, reverse=1))
    for i in range(0, 20):
        print(out[i])


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
if __name__ == '__main__':
    main()
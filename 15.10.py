__author__ = 'a'
import os


def show_files(dir_path):
    count = 0
    for cur_path, dir_names, file_names in os.walk(dir_path):
        for file_name in file_names:
            count += os.path.getsize(os.path.join(cur_path, file_name))
    return count

print(show_files('/home/a/Загрузки'))



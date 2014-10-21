__author__ = 'rezenter'
import os
import hashlib
files = {}
first = ''
second = ''


def hashing(path):
    hash_obj = hashlib.md5()
    chunk = 4096
    file_obj = open(path, "rb")
    while True:
        file_chunk = file_obj.read(chunk)
        if not file_chunk:
            break
        hash_obj.update(file_chunk)
    file_obj.close()
    return hash_obj.hexdigest()


def files_equal(file1_path, file2_path):
    global files
    global first
    global second
    if first == '':
        first = file1_path
    if second == '':
        first = file2_path
    if not os.path.exists(file1_path) or not os.path.exists(file2_path):
        return None
    if not os.path.isfile(file1_path) or not os.path.isfile(file2_path):
        return None
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False
    if len(files) == 128:  # so we should delete the latest note
        del files[first]   # i delete the first element, and i will have to delete it again at least after 128 scans
        first = file1_path
    if file1_path not in files or files[file1_path][1] != os.stat(file1_path).st_mtime_ns:
        files[file1_path] = [hashing(file1_path), os.stat(file1_path).st_mtime_ns]
    if len(files) == 128:
        del files[second]
        second = file2_path
    if file2_path not in files or files[file2_path][1] != os.stat(file2_path).st_mtime_ns:
        files[file2_path] = [hashing(file2_path), os.stat(file2_path).st_mtime_ns]
    if files[file1_path][0] != files[file2_path][0]:
        return False
    chunk = 4096
    file1 = open(file1_path, 'rb')
    file2 = open(file2_path, 'rb')
    while True:
        file1_chunk = file1.read(chunk)
        file2_chunk = file2.read(chunk)
        if not file1_chunk or not file2_chunk:
            break
        if not file2_chunk == file1_chunk:
            file1.close()
            file2.close()
            return False
    file1.close()
    file2.close()
    return True


def find_eq_files(file_path, search_dir_path):
    if not os.path.exists(file_path) or not os.path.exists(search_dir_path):
        return None
    if not os.path.isfile(file_path) or not os.path.isdir(search_dir_path):
        return None
    result = []
    for cur_path, dir_names, file_names in os.walk(search_dir_path):
        for file_name in file_names:
            tmp = files_equal(file_path, os.path.join(cur_path, file_name))
            if tmp:
                result.append(os.path.join(cur_path, file_name))
    return result

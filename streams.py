import sys


class TextStream(object):
    @staticmethod
    def create(typ, args):
        if typ == "file":
            return FileTextStream.create(*args)
        elif typ == "console":
            return ConsoleTextStream.create()
        return StringTextStream.create()

    def readLine(self):
        """Returns line from current read position"""
        raise Exception("Not implemented")

    def append(self, string):
        """Append string to the stream"""
        raise Exception("Not implemented")

    def close(self):
        """Releases all the used resources"""
        raise Exception("Not implemented")


class ConsoleTextStream(TextStream):
    _instanse = None
    @staticmethod
    def create():
        if ConsoleTextStream._instanse is None:
            ConsoleTextStream._instanse = ConsoleTextStream()
        return ConsoleTextStream._instanse

    def readLine(self):
        return sys.stdin.readline()

    def append(self, string):
        sys.stdout.write(string)

    def close(self):
        sys.stdin.close()
        sys.stdout.close()


class FileTextStream(TextStream):
    _instance = {}
    @staticmethod
    def create(path):
        if len(FileTextStream._instance) == 0:
            FileTextStream._instance[path] = FileTextStream(path)
        elif path not in FileTextStream._instance.keys():
            FileTextStream._instance[path] = FileTextStream(path)
        return FileTextStream._instance[path]

    def __init__(self, file_path):
        self._file = open(file_path, "w+")
        self._writePos = 0
        self._readPos = 0

    def readLine(self):
        self._file.seek(self._readPos)
        line = self._file.readline()
        self._readPos = self._file.tell()
        return line

    def append(self, string):
        self._file.seek(self._writePos)
        self._file.write(string)
        self._writePos = self._file.tell()

    def close(self):
        self._file.close()


class StringTextStream(TextStream):
    @staticmethod
    def create():
        return StringTextStream()

    def __init__(self):
        self._str = ""

    def readLine(self):
        newline_ix = self._str.find("\n")
        if newline_ix == -1:
            ret = self._str
            self._str = ""
            return ret
        else:
            ret = self._str[:newline_ix + 1]
            self._str = self._str[newline_ix + 1:]
            return ret

    def append(self, string):
        self._str += string

    def close(self):
        pass

    def getString(self):
        return str(self._str)
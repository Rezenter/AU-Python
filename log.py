__author__ = 'rezenter'
from streams import *


class Logger:
    _currentStream = StringTextStream.create()
    _flag = True
    @staticmethod
    def setStream(stream):
        if Logger._flag:
            Logger._currentStream = stream
            Logger._flag = False
        return Logger._currentStream

    @staticmethod
    def error(string):
        Logger._currentStream.append("ERROR: " + string + "\n")

    @staticmethod
    def warning(string):
        Logger._currentStream.append("WARNING: " + string + "\n")

    @staticmethod
    def info(string):
        Logger._currentStream.append("INFO: " + string + "\n")
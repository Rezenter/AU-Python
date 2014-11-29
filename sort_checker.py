__author__ = 'rezenter'
import random
import time


class Sort:
    @staticmethod
    def timeOfSort(sort1):
        n = 10000
        m = 1000
        time1 = 0
        for i in range(m):
            lst1 = [random.randint(0, 10000) for a in range(n)]
            tmp = time.time()
            sort1.sort(lst1)
            time1 += time.time() - tmp
        time1 = time1/m
        return time1

    @staticmethod
    def compare(sort1, sort2):
        n = 10000
        m = 1000
        time1 = 0
        time2 = 0
        for i in range(m):
            lst1 = [random.randint(0, 10000) for a in range(n)]
            lst2 = list(lst1)
            tmp = time.time()
            sort1.sort(lst1)
            time1 += time.time() - tmp
            tmp = time.time()
            sort2.sort(lst2)
            time2 += time.time() - tmp
        time1 = time1/m
        time2 = time2/m
        return [time1, time2]

    def sort(self, lst):
        pass

class BubbleSort(sort):
    def sort(self):
        pass
__author__ = 'rezenter'


class Q:
    def __init__(self, up = 0, down = 1):
        self._a = up
        self._b = down

    #get methods used to prevent access to "protected" values
    def getUp(self):
        return self._a

    def getDown(self):
        return self._b

    def __add__(self, q):
        return Q(self.getUp() * q.getDown() + q.getUp() * self.getDown(), self.getDown()*q.getDown())

    def __str__(self):
        return str(self._a) + '/' + str(self._b)
a = Q(2, 3) + Q(3, 4)
print(a)
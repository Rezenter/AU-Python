__author__ = 'rezenter'


class Node:
    def __init__(self, v=None, l=None, r=None):
        self._left = l
        self._right = r
        self._value = v

    def setLeft(self, l):
        self._left = l

    def setRight(self, r):
        self._right = r

    def setValue(self, v):
        self._value = v

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def getValue(self):
        return self._value

    def __str__(self):
        return "Node ( " + str(self._value) + " )"

    def __bool__(self):
        return self._value is not None

    def strChilds(self, lev=0):
        res = "%s%s" % ("    "*lev, self) + "\n"
        if self.getLeft() is not None:
            res += self.getLeft().strChilds(lev+1)
        if self.getRight() is not None:
            res += self.getRight().strChilds(lev+1)
        return res

    def lstChilds(self):
        res = [self]
        if self.getLeft() is not None:
            res.extend(self.getLeft().lstChilds())
        if self.getRight() is not None:
            res.extend(self.getRight().lstChilds())
        return res


class Tree:
    def __init__(self, root):
        self._rootNode = root

    def getRoot(self):
        return self._rootNode

    def __iter__(self):
        self.listed = self._rootNode.lstChilds()
        return self

    def __next__(self):
        if len(self.listed) != 0:
            return self.listed.pop(0)
        else:
            raise StopIteration

    def __str__(self):
        return self._rootNode.strChilds()

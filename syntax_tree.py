__author__ = 'rezenter'
import tree


class ASTNode(tree.Node):
    @staticmethod
    def execute(self):
        raise Exception("nope")


class IntLiteralNode(ASTNode):
    def execute(self):
        return self._value


class UnaryOpNode(ASTNode):
    def getArg(self):
        return self._left.getValue()

    def getMnemonic(self):
        return self._value


class UnMinusNode(UnaryOpNode):
    def __init__(self, node):
        UnaryOpNode.__init__(self, '-', node)

    def execute(self):
        return -1*self._left.execute()


class PrintNode(UnaryOpNode):
    def __init__(self, node):
        UnaryOpNode.__init__(self, 'print', node)

    def execute(self):
        x = self._left.execute()
        print(x)
        return x


class BinaryOpNode(ASTNode):
    def getMnemonic(self):
        return self._value

    def getArgL(self):
        return self._left.getValue()

    def getArgR(self):
        return self._right.getValue()


class BinPlusNode(BinaryOpNode):
    def __init__(self, l, r):
        BinaryOpNode.__init__(self, '+', l, r)

    def execute(self):
        return self._left.execute() + self._right.execute()


class BinMinusNode(BinaryOpNode):
    def __init__(self, l, r):
        BinaryOpNode.__init__(self, '-', l, r)

    def execute(self):
        return self._left.execute() - self._right.execute()


class BinMulNode(BinaryOpNode):
    def __init__(self, l, r):
        BinaryOpNode.__init__(self, '*', l, r)

    def execute(self):
        return self._left.execute() * self._right.execute()


class BinDivNode(BinaryOpNode):
    def __init__(self, l, r):
        BinaryOpNode.__init__(self, '//', l, r)

    def execute(self):
        return self._left.execute() // self._right.execute()


class AST(tree.Tree):
    def execute(self):
        if self.getRoot().getValue() == "print":
            return PrintNode(self.getRoot().getLeft()).execute()
        elif self.getRoot().getValue() == "-":
            if self.getRoot().getRight() is None:
                return UnMinusNode(self.getRoot().getLeft()).execute()
            return BinMinusNode(AST(self.getRoot().getLeft()).execute(), AST(self.getRoot().getRight()).execute())
        elif self.getRoot().getValue() == "+":
            return BinPlusNode(AST(self.getRoot().getLeft()).execute(), AST(self.getRoot().getRight()).execute())
        elif self.getRoot().getValue() == "*":
            return BinMulNode(AST(self.getRoot().getLeft()).execute(), AST(self.getRoot().getRight()).execute())
        elif self.getRoot().getValue() == "//":
            return BinDivNode(AST(self.getRoot().getLeft()).execute(), AST(self.getRoot().getRight()).execute())
__author__ = 'rezenter'
import tree


class ASTNode(tree.Node):
    def execute(self):
        raise Exception("nope")


class IntLiteralNode(ASTNode):
    def execute(self):
        return self.getValue()


class UnaryOpNode(ASTNode):
    def getArg(self):
        return self.getLeft().getValue()

    def getMnemonic(self):
        return self.getValue()


class UnMinusNode(UnaryOpNode):
    def __init__(self, node):
        UnaryOpNode.__init__(self, '-', node)

    def execute(self):
        return -1*self.getLeft().execute()


class PrintNode(UnaryOpNode):
    def __init__(self, node):
        UnaryOpNode.__init__(self, 'print', node)

    def execute(self):
        x = self.getLeft().execute()
        print(x)
        return x


class BinaryOpNode(ASTNode):
    def getMnemonic(self):
        return self.getValue()

    def getArgL(self):
        return self.getLeft().getValue()

    def getArgR(self):
        return self.getRight().getValue()


class BinPlusNode(BinaryOpNode):
    def __init__(self, l, r):
        BinaryOpNode.__init__(self, '+', l, r)

    def execute(self):
        return self.getLeft().execute() + self.getRight().execute()


class BinMinusNode(BinaryOpNode):
    def __init__(self, l, r):
        BinaryOpNode.__init__(self, '-', l, r)

    def execute(self):
        return self.getLeft().execute() - self.getRight().execute()


class BinMulNode(BinaryOpNode):
    def __init__(self, l, r):
        BinaryOpNode.__init__(self, '*', l, r)

    def execute(self):
        return self.getLeft().execute() * self.getRight().execute()


class BinDivNode(BinaryOpNode):
    def __init__(self, l, r):
        BinaryOpNode.__init__(self, '//', l, r)

    def execute(self):
        return self.getLeft().execute() // self.getRight().execute()


class AST(tree.Tree):
    def execute(self):
        return self.getRoot().execute()


def parseExpr(expr):
    expr = expr.split()
    buffer = []
    flag = True
    e = 0
    for i in expr:
        try:
            i = int(i)
            buffer.append(IntLiteralNode(i))
        except ValueError:
            try:
                if i == "print":
                    buffer.append(PrintNode(buffer.pop()))
                elif i == "!":
                    buffer.append(UnMinusNode(buffer.pop()))
                elif i == "+":
                    buffer.append(BinPlusNode(buffer.pop(), buffer.pop()))
                elif i == '-':
                    r = buffer.pop()
                    buffer.append(BinMinusNode(buffer.pop(), r))
                elif i == "*":
                    buffer.append(BinMulNode(buffer.pop(), buffer.pop()))
                elif i == "/" or i == '//':
                    r = buffer.pop()
                    buffer.append(BinDivNode(buffer.pop(), r))
            except IndexError:
                e = i
                flag = False
                break
    if flag and len(buffer) == 1:
        return AST(PrintNode(buffer[0]))
    elif not flag:
        return AST(IntLiteralNode("Not enough args for " + str(e)))
    return AST(IntLiteralNode("Too many args in expr"))
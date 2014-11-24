from tree import *

def test(assertion, error_str = ""):
    if not assertion:
        raise Exception(error_str)

def test_node_basics():

    node = Node(1)

    test(node.getValue() == 1)


    test(node.getLeft() == None)

    test(node.getRight() == None)

    node.setLeft(node)

    test(node.getLeft() == node)

    node.setRight(node)

    test(node.getRight() == node)

    node.setValue(100)

    test(node.getValue() == 100)


def test_node_str():
    node = Node(1)
    test(str(node) == "Node ( 1 )")

def test_node_bool():
    node = Node()
    test(not node)
    node = Node(0)
    test(node)

def test_tree_basics():
    root = Node(0)
    tree = Tree(root)
    test(tree.getRoot() == root)

def create_full_tree():
    node31 = Node(31)
    node32 = Node(32)
    node33 = Node(33)
    node34 = Node(34)
    node35 = Node(35)
    node36 = Node(36)
    node37 = Node(37)
    node38 = Node(38)

    node21 = Node(21, node31, node32)
    node22 = Node(22, node33, node34)
    node23 = Node(23, node35, node36)
    node24 = Node(24, node37, node38)

    node11 = Node(11, node21, node22)
    node12 = Node(12, node23, node24)

    root = Node(0, node11, node12)
    return Tree(root)

def test_full_tree_iter():
    tree = create_full_tree()
    it = iter(tree)
    node_vals_set = {
        0,
        11, 12,
        21, 22, 23, 24,
        31, 32, 33, 34, 35, 36, 37, 38
    }
    for node in it:
        node_vals_set.remove(node.getValue())
    test(len(node_vals_set) == 0)

def test_full_tree_str():
    tree = create_full_tree()

    ref_str_tree = """Node ( 0 )
    Node ( 11 )
        Node ( 21 )
            Node ( 31 )
            Node ( 32 )
        Node ( 22 )
            Node ( 33 )
            Node ( 34 )
    Node ( 12 )
        Node ( 23 )
            Node ( 35 )
            Node ( 36 )
        Node ( 24 )
            Node ( 37 )
            Node ( 38 )
"""
    #use this for debugging
    print(repr(str(tree)))
    print(repr(ref_str_tree))
    test(str(tree) == ref_str_tree)


def main():
    test_node_basics()
    test_node_str()
    test_node_bool()
    test_tree_basics()
    test_full_tree_iter()
    test_full_tree_str()
    print("Success!")

if __name__ == "__main__":
    main()
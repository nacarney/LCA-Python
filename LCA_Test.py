import unittest
from LCA import Node
from LCA import lca
from LCA import treeToString

class TestLCA(unittest.TestCase):
    def test_lca_output(self):

        root = Node(20)
        root.left = Node(8)
        root.right = Node(22)
        root.left.left = Node(4)
        root.left.right = Node(12)
        root.left.right.left = Node(10)
        root.left.right.right = Node(14)

        n1 = 10
        n2 = 14
        assert lca(root, n1, n2).data == 12


    def test_lca_output_2(self):

        root = Node(15)
        root.left = Node(12)
        root.left.left = Node(11)
        root.left.right = Node(13)
        root.right = Node(18)
        root.right.left = Node(17)

        n1 = 11
        n2 = 13

        #               _15_
        #              /
        #
        #
        #



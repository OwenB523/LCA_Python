import unittest
from LCA import *


class TestLCA(unittest.TestCase):

    def test_empty_tree(self):
        tree = Tree()
        self.assertEqual(tree.find_LCA(1, 2), None)

    def test_single_node(self):
        tree = Tree()
        tree.put(2)
        self.assertEqual(tree.find_LCA(2, 2), None)
        self.assertEqual(tree.find_LCA(2, 1), None)

    def test_identical(self):
        tree = Tree()
        nodes = [2, 1, 4, 4]
        for x in nodes:
            tree.put(x)
        self.assertEqual(tree.find_LCA(4, 4), None)
        self.assertEqual(tree.find_LCA(1, 1), None)

    def test_LCA(self):
        nodes = [30, 8, 52, 3, 20, 10, 29, 62]
        tree = Tree()
        for x in nodes:
            tree.put(x)
        self.assertEqual(tree.find_LCA(3, 8), 30)
        self.assertEqual(tree.find_LCA(3, 29), 8)
        self.assertEqual(tree.find_LCA(10, 29), 20)
        self.assertEqual(tree.find_LCA(3, 62), 30)
        self.assertEqual(tree.find_LCA(62, 52), 30)
        self.assertEqual(tree.find_LCA(4, 29), None)



if __name__ == '__main__':
    unittest.main()

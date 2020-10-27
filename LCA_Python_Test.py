import unittest
import LCA_Python

class TestLCA(unittest.TestCase):

    def test_RegularTree(self):
        #print("Test1: Test Regular Tree:")
        root = LCA_Python.Node(1)
        root.left = LCA_Python.Node(2)
        root.right = LCA_Python.Node(3)
        root.left.left = LCA_Python.Node(4)
        root.left.right = LCA_Python.Node(5)
        root.right.left = LCA_Python.Node(6)
        root.right.right = LCA_Python.Node(7)

        #print(root)

        self.assertEqual(3, LCA_Python.findLCA(root, 6, 7), "3 should be the lowest common ancestor of 6 and 7")

    def test_NullTree(self):
        #print("Test2: Test Null Tree:")
        root = None
        self.assertEqual(-1, LCA_Python.findLCA(root, 6, 7), " The output should be -1 since the tree is empty")


    def test_TwoNodesNotPresent(self):
        #print("Test3: testTwoNodesNotPresent:")
        root = LCA_Python.Node(1)
        self.assertEqual(-1, LCA_Python.findLCA(root, 6, 7), " The output should be -1 both nodes are missing")

    def test_OneNodeNotPresent(self):
        #print("Test4: testOneNodeNotPresent:")
        root = LCA_Python.Node(1)
        root.left = LCA_Python.Node(2)
        self.assertEqual(-1, LCA_Python.findLCA(root, 2, 3), " The output should -1 since one of the nodes is missing")

#Reminder if you don't put the word test in python functions they won't work!!
if __name__ == '__main__':
    unittest.main()

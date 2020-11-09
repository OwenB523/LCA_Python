class Node(object):

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __lt__(self, key):
        return self.key < key

    def __gt__(self, key):
        return self.key > key

    def __eq__(self, key):
        return self.key == key


class Tree(object):

    def __init__(self):
        self.root = None

    def put(self, key):
        if not (self.node_check(key)):
            self.root = self._put(self.root, key)

    def _put(self, node, key):
        if node is None:
            node = Node(key)

        if key < node:
            node.left = self._put(node.left, key)
        elif key > node:
            node.right = self._put(node.right, key)
        else:
            node.key = key

        return node

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        while node is not None:
            if key < node:
                node = node.left
            elif key > node:
                node = node.right
            else:
                return node.key
        return None

    def find_LCA(self, a, b):
        if a == b:
            return
        else:
            return self._find_LCA(self.root, a, b)

    def _find_LCA(self, node, a, b):
        if node is None:
            return None
        if a > node and b > node:
            if node.right is None:
                return None
            if node.right == a or node.right == b:
                return node.key

            return self._find_LCA(node.right, a, b)

        elif a < node and b < node:
            if node.left is None:
                return None

            if node.left == a or node.left == b:
                return node.key

            return self._find_LCA(node.left, a, b)

        elif a == self.root or b == self.root:
            return None

        else:
            if self._node_check(node, a):
                if self._node_check(node, b):
                    return node.key
                else:
                    return None
            else:
                return None

    def node_check(self, key):
        return self._node_check(self.root, key)

    def _node_check(self, node, key):
        return not self._get(node, key) is None

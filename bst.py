class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, node, result):
        if node is not None:
            result.append(node.key)  # Visit the root
            self._preorder_traversal(node.left, result)  # Traverse the left subtree
            self._preorder_traversal(node.right, result)  # Traverse the right subtree
        return result

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, node, result):
        if node is not None:
            self._postorder_traversal(node.left, result)  # Traverse the left subtree
            self._postorder_traversal(node.right, result)  # Traverse the right subtree
            result.append(node.key)  # Visit the root
        return result

# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(17)

print("Preorder Traversal:", bst.preorder_traversal())  # Output: [10, 5, 2, 7, 15, 12, 17]
print("Postorder Traversal:", bst.postorder_traversal())  # Output: [2, 7, 5, 12, 17, 15, 10]

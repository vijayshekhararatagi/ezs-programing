class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def delete(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.min_value_node(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def search(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self.search(node.left, value)
        return self.search(node.right, value)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)

# Example usage
if __name__ == "__main__":
    tree = AVLTree()
    for value in [10, 20, 30, 40, 50]:
        tree.insert_value(value)

    print("In-order traversal after insertions:")
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            print(node.value, end=" ")
            inorder_traversal(node.right)

    inorder_traversal(tree.root)
    print()

    tree.delete_value(20)
    print("In-order traversal after deletion of 20:")
    inorder_traversal(tree.root)
    print()

    result = tree.search_value(30)
    print("Node found" if result else "Node not found")

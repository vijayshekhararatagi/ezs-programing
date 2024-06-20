class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def level_order_traversal(self, root):
        if root is None:
            return
        q = [root]
        q.append(None)
        while len(q) > 0:
            curr = q.pop(0)
            if curr is None:
                if len(q) == 0:
                    break
                else:
                    print()
                    q.append(None)
            else:
                print(curr.value, end=' ')
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)

if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    root.right.left.right = Node(8)
    root.right.left.left = Node(9)

    root.right.right.left = Node(10)
    root.right.right.right = Node(11)

    root.level_order_traversal(root)

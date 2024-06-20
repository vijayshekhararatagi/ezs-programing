class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class NodeData:
    def __init__(self, node, key):
        self.node = node
        self.key = key

def bottomview(root):
    if root is None:
        return
    
    # Initialize queue for level order traversal
    temp = NodeData(root, 0)
    q = [temp]
    
    # Dictionary to store the bottom view nodes
    key_d = {}
    
    while len(q) > 0:
        curr = q.pop(0)
        
        # Update the dictionary with the current node for each horizontal distance
        key_d[curr.key] = curr.node.value
        
        # Enqueue left child with horizontal distance decreased by 1
        if curr.node.left is not None:
            temp = NodeData(curr.node.left, curr.key - 1)
            q.append(temp)
        
        # Enqueue right child with horizontal distance increased by 1
        if curr.node.right is not None:
            temp = NodeData(curr.node.right, curr.key + 1)
            q.append(temp)
    
    # Print the bottom view
    for key in sorted(key_d.keys()):
        print(key_d[key], end=' ')
    print()

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
    
    root.right.right.left.left = Node(12)
    root.right.right.left.right = Node(13)

    bottomview(root)

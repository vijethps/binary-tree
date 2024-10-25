
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left, data)
        else:  
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right, data)


if __name__ == "__main__":
    n = int(input()) 
    values = list(map(int, input().strip().split()))

    binary_tree = BinaryTree()  

    for value in values:
        binary_tree.insert(value)  

    print("Tree structure successfully built!")

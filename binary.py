# Tree mean nodes connected by edges
# It is non-linear data structure
# one node mark as node
# every node can have an arbiatry number of child node

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
 # Compare the new value with the parent node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
root = Node(10)
root.insert(7)
root.insert(14)
root.insert(3)
root.insert(2)
root.PrintTree()
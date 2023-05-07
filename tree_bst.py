class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        t = self.root
        while True:
            if t.value > new_val:
                if not t.left:
                    t.left = Node(new_val)
                    return
                t = t.left
                continue

            if t.value < new_val:
                if not t.right:
                    t.right = Node(new_val)
                    return
                t = t.right
                continue

            return
                
            

    def search(self, find_val):
        t = self.root
        while True:
            if t.value == find_val:
                return True
            if t.value > find_val:
                if not t.left:
                    return False
                t = t.left
                continue
            if t.value < find_val:
                if not t.right:
                    return False
                t = t.right
                continue
            return False

    

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
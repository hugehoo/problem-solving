class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    # recursive
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def find(self, key):
        return self._find_value(self.root, key)
    
    # recursive
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
    
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    
    # recursive
    def _delete_value(self, node, key):
        if node is None:
            return node, False
        
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the most left of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted
    
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)
    
    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)
# print(bst.find(4))
# print(bst.find(11))
print(bst.pre_order_traversal())
# print()
# print(bst.in_order_traversal())
# print()
# print(bst.post_order_traversal())

# # Find
# print(bst.find(15))  # True
# print(bst.find(17))  # False
#
# # Delete
# print(bst.delete(55))  # True
# print(bst.delete(14))  # True
# print(bst.delete(11))  # False

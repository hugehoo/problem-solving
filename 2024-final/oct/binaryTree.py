class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def set_left(self, node):
        self.left = node
    
    def set_right(self, node):
        self.right = node
    
    def set_value(self, value):
        self.value = value
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_value(self):
        return self.value


class BST:
    def __init__(self):
        self.head: Node | None = None
    
    def search(self, value):
        if self.head is None:
            return False, None
        
        depth = 0
        node = self.head
        
        while node:
            if value == node.get_value():
                return True, depth
            elif value < node.get_value():
                node = node.get_left()
            else:
                node = node.get_right()
            depth += 1
        
        return False, None
    
    def traversal(self, node, option):
        if node is None:
            return
        if option == 1:  # Preorder
            print(node.value, end=" ")
            self.traversal(node.get_left(), option)
            self.traversal(node.get_right(), option)
        elif option == 2:  # Inorder
            self.traversal(node.get_left(), option)
            print(node.value, end=" ")
            self.traversal(node.get_right(), option)
        elif option == 3:  # Postorder
            self.traversal(node.get_left(), option)
            self.traversal(node.get_right(), option)
            print(node.value, end=" ")
    
    def print_tree(self, option=1):
        if option == 1:
            print('preorder:', end=' ')
        elif option == 2:
            print('inorder:', end=' ')
        elif option == 3:
            print('postorder:', end=' ')
        
        print("head: ", self.head.value)
        self.traversal(self.head, option)
        print("")
    
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while True:
                if value < node.get_value():
                    if node.get_left() is None:
                        node.set_left(Node(value))
                        break
                    else:
                        node = node.get_left()
                else:
                    if node.get_right() is None:
                        node.set_right(Node(value))
                        break
                    else:
                        node = node.get_right()
    
    def delete(self, value):
        if self.head is None:
            return False
        node = self.head
        parent = self.head
        check = False
        # if value == node.get_value():
        # if value < node.get_value():
        


# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def set_left(self, node):
#         self.left = node
#
#     def set_right(self, node):
#         self.right = node
#
#     def set_value(self, node):
#         self.value = node
#
#     def get_left(self):
#         return self.left
#
#     def get_right(self):
#         return self.right
#
#     def get_value(self):
#         return self.value
#
#
# class BST:
#     def __init__(self):
#         self.head: Node | None = None
#
#     def insert(self, value):
#         if self.head is None:
#             self.head = value
#         else:
#             node = self.head
#             while True:
#                 if value < node.get_value():
#                     if node.get_left() is None:
#                         node.set_left(Node(value))
#                         break
#                     else:
#                         node = node.get_left()
#                 else:
#                     if node.get_right() is None:
#                         node.set_right(Node(value))
#                         break
#                     else:
#                         node = node.get_right()
#
#
#     def search(self, value) -> (bool, int):
#         if self.head is None:
#             return False, None
#
#         depth = 0
#         node = self.head
#
#         while node:
#             if value == node.get_value():
#                 return True, depth
#             elif value < node.get_value():
#                 node = node.get_left()
#             else:
#                 node = node.get_right()
#             depth += 1
#         return False, None
#
#     def in_traversal(self, node):
#         self.in_traversal(self.head.get_left())
#         print(node.get_value)
#         self.in_traversal(self.head.get_right())
#
        
        


if __name__ == "__main__":
    bst = BST()
    bst.insert(6)
    bst.insert(1)
    bst.insert(7)
    bst.insert(2)
    bst.insert(9)
    bst.insert(4)
    bst.print_tree(1)
    # print(bst.search(8))
    # print(bst.search(7))
    # print(bst.in_traversal(1))
    

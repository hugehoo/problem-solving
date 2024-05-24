# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    
    # version 1
    def maxDepth(self, root):
        if not root:
            return 0
        print(root.left.val if root.left is not None else None)
        print(root.right.val if root.right is not None else None)
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    # version 2
    def maxDepth(self, root):
        def dfs(node, count):
            if node is None:
                return count
            count += 1
            return max(dfs(node.left, count), dfs(node.right, count))
        
        return dfs(root, 0)


root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
s = Solution()
s.maxDepth(root)

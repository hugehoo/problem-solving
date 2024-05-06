# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, count):
            if node is None:
                return count
            count += 1
            return max(dfs(node.left, count), dfs(node.right, count))
        return dfs(root, 0)


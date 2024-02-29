from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        nums = defaultdict(list)
        
        def bfs(node: TreeNode, count):
            if node is None:
                return
            else:
                nums[count].append(node.val)
            bfs(node.left, count + 1)
            bfs(node.right, count + 1)
        
        bfs(root, 1)
        
        result = [round(sum(nums[k]) / len(nums[k]), 5) for k in nums.keys()]
        return result


s = Solution()
t = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None),
             right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None),
                            right=TreeNode(val=7, left=None, right=None)))
print(s.averageOfLevels(t))



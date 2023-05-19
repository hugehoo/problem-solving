# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s1 = self.method_name(l1)
        s2 = self.method_name(l2)
        return list(str(s1 + s2))[::-1]

    def method_name(self, l1):
        l1_list = []
        curr_node = l1
        while True:
            if curr_node.next:
                l1_list.append(str(curr_node.val))
                curr_node = curr_node.next
            else:
                if curr_node.val:
                    l1_list.append(str(curr_node.val))
                break
        return int(''.join(l1_list[::-1]))



s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1, 0, 3, 5, 9, 12], 2))

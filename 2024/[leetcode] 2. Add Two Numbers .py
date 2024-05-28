# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_string = ""
        while l1:
            l1_string = str(l1.val) + l1_string
            l1 = l1.next
        
        l2_string = ""
        while l2:
            l2_string = str(l2.val) + l2_string
            l2 = l2.next
        
        l_sum = str(int(l1_string) + int(l2_string))
        
        l3 = ListNode(int(l_sum[-1]))
        itr = l3
        
        for numIdx in range(-2, -len(l_sum) - 1, -1):
            itr.next = ListNode(int(l_sum[numIdx]))
            itr = itr.next
        return l3


l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
s = Solution()
print(s.addTwoNumbers(l1, l2))

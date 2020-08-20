class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        n1 = 0
        i = 0
        cur = l1
        while cur.next:
            n1 += cur.val * (10 ** i)
            i += 1
            cur = cur.next
        print(n1)

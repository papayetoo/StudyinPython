# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        left = l1
        right = l2
        head = ListNode()
        ret = head

        while left and right:
            if left.val <= right.val:
                head.next = ListNode(left.val)
            else:
                head.next = ListNode(right.val)
            head = head.next

        if not left:
            head.next = right
        if not right:
            head.next = left

        return ret.next

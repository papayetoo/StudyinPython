# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        currentNode = head
        lst = []
        while currentNode:
            lst.append(currentNode)
            currentNode = currentNode.next

        newK = k % len(lst)
        lst = lst[-newK:] + lst[:-newK]
        for i in range(len(lst) - 1):
            lst[i].next = lst[i + 1]
        lst[-1].next = None
        return lst[0]

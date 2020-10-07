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

    def rotateRight2(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return None

        curNode = head
        prev = None
        n = 0
        # traverse to the last node
        while curNode and curNode.next:
            prev = curNode
            curNode = curNode.next
            n += 1
        n += 1
        if k % n == 0:
            return head

        i = 0
        k %= n
        startNode = head
        while i < n - k - 1:
            startNode = startNode.next
            i += 1
        ans = startNode.next
        startNode.next = None
        curNode.next = head

        return ans




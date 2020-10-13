# Definition for singly-linked list.
# MERGE SORT 구현...
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        def getHalf(curNode: ListNode) -> ListNode:
            if not curNode:
                return curNode

            slow = curNode
            fast = curNode

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def sortedMerge(a: ListNode, b: ListNode):

            if not a:
                return b
            if not b:
                return a

            if a.val <= b.val:
                result = a
                result.next = sortedMerge(a.next, b)
            else:
                result = b
                result.next = sortedMerge(a, b.next)
            return result

        def mergeSort(h: ListNode):

            if not h or not h.next:
                return h

            middle = getHalf(h)
            nextToMiddle = middle.next

            middle.next = None

            left = mergeSort(h)
            right = mergeSort(nextToMiddle)

            sortedList = sortedMerge(left, right)
            return sortedList

        return mergeSort(head)

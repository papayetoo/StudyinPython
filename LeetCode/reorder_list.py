class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next

        length = len(nodes)
        pairs = []
        for i in range(length // 2 + 1 if length % 2 == 1 else length // 2):
            pairs.append((i, length -i - 1))

        for i in range(len(pairs)):
            nodes[pairs[i][0]].next = nodes[pairs[i][1]]
            nodes[pairs[i][1]].next = nodes[pairs[i+1][0]] if i + 1 < len(pairs) else None

    def reorderList2(self, head: ListNode) -> None:

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        #step2 : reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp
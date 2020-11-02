# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        root = None
        current = head
        end = None
        while current:
            node = ListNode(current.val)
            if not root:
                root = node
                end = root
            else:
                if end.val <= current.val:
                    end.next = node
                    end = node
                else:
                    cur, pre = root, None
                    while cur:
                        if cur.val < current.val:
                            pre = cur
                            cur = cur.next
                        else:
                            if pre:
                                pre.next = node
                                node.next = cur
                            else:
                                pre = node
                                node.next = cur
                                root = pre
                            break
            current = current.next
        return root

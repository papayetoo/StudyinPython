# 1. Brute Force로 풀 수 있음.
# 2. Divied and Conquer 로 풀 수 있음. 병합 정렬을 응용.
# 3. 우선순위큐를 이용
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def helper(l: ListNode, r: ListNode) -> ListNode:
            answer = ListNode()
            res = answer
            curL = l
            curR = r
            while curL and curR:
                if curL.val > curR.val:
                    res.next = curR
                    res = res.next
                    curR = curR.next
                    continue
                else:
                    res.next = curL
                    res = res.next
                    curL = curL.next
                    continue

            if curL:
                res.next = curL

            if curR:
                res.next = curR

            return answer.next

        k = len(lists)
        # lists.sort(key=lambda x: x.val if x else float('inf'))
        answer = None
        for i in range(k):
            answer = helper(answer, lists[i])
        return answer
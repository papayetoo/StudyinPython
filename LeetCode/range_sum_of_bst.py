# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        q = deque([root])
        answer = 0
        while q:
            node = q.popleft()
            if low <= node.val <= high:
                answer += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return answer
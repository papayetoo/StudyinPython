# Problem related to BFS(Breast-First Search)

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        level = 1
        q = deque([(root, level)])

        if not root:
            return 0

        while q:
            curNode, curLevel = q.popleft()
            if not curNode.left and not curNode.right:
                return curLevel
            if curNode.right:
                q.append((curNode.right, curLevel + 1))
            if curNode.left:
                q.append((curNode.left, curLevel + 1))

        return 0


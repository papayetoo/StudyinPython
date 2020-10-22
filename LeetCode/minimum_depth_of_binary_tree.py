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
        # deque Solution
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

    def minDepth2(self, root: TreeNode) -> int:
        # Recurssive Solution
        if not root:
            return 0

        lheight = float('inf')
        rheight = float('inf')

        if not root.left and not root.right:
            return 1

        if root.left:
            lheight = min(lheight, 1 + self.minDepth(root.left))
        if root.right:
            rheight = min(rheight, 1 + self.minDepth(root.right))

        return min(lheight, rheight)
from collections import deque
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        def bfs():
            result = []
            level = 0
            curNode = root
            queue = deque()
            queue.append([level, curNode])

            while queue:
                curLevel, curNode = queue.popleft()
                if len(result) == curLevel:
                    result.insert(curLevel, curNode.val)
                elif len(result) == curLevel + 1:
                    result[curLevel] = curNode.val
                if curNode.left:
                    queue.append([curLevel + 1, curNode.left])
                if curNode.right:
                    queue.append([curLevel + 1, curNode.right])
            return result

        answer = bfs() if root else []
        return answer


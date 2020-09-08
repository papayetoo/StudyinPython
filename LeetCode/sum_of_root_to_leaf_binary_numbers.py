from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, ''))
        ans = 0
        while queue:
            front = queue.pop()
            if front[0]:
                if not front[0].left and not front[0].right:
                    # print(front[1] + str(front[0].val))
                    ans += int(front[1] + str(front[0].val), 2)
                else:
                    queue.append((front[0].left, front[1] + str(front[0].val)))
                    queue.append((front[0].right, front[1] + str(front[0].val)))

        return ans

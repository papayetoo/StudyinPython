# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node: TreeNode):
            if not node:
                return (0, 0)

            l = helper(node.left)
            r = helper(node.right)
            rob = node.val + l[1] + r[1]
            notrob = max(l) + max(r)

            return (rob, notrob)

        answer = helper(root)
        return max(answer)

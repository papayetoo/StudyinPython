# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:


        def postorder(node: TreeNoe):
            if not node:
                return 0

            l = postorder(node.left)
            r = postorder(node.right)
            return abs(l - r)

        result = postorder(root)
        print(result)
        return 0
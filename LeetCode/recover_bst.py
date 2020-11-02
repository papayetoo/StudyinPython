# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = TreeNode(float('-inf'))

        def inorder(current: TreeNode):
            nonlocal prev, first, second
            if not current:
                return

            inorder(current.left)
            if not first and prev.val >= current.val:
                first = prev
            if first and prev.val >= current.val:
                second = current
            inorder(current.right)

        inorder(root)
        first.val, second.val = second.val, second.val
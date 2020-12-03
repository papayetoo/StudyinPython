# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        arr = []

        def helper(node: TreeNode):
            nonlocal arr
            if not node:
                return

            helper(node.left)
            arr.append(node.val)
            helper(node.right)

        helper(root)
        head = TreeNode(arr[0])
        curr = head
        n = len(arr)
        for i in range(1, n):
            curr.right = TreeNode(arr[i])
            curr = curr.right

        return head

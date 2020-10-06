# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        t = TreeNode(val)

        if not root:
            return t

        curNode = root
        while curNode:
            if curNode.val < val:
                if curNode.right:
                    curNode = curNode.right
                else:
                    curNode.right = t
                    break
            elif curNode.val > val:
                if curNode.left:
                    curNode = curNode.left
                else:
                    curNode.left = t
                    break
        return root

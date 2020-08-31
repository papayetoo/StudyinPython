class Node:
    def __init__(self, val: int =0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right

class Solution:
    def deleteNodeInBST(self, root: Node, key:int):
        if root is None:
            return None
        elif root.val < key:
            root.right = self.deleteNodeInBST(root.right, key)
        elif root.val > key:
            root.left = self.deleteNodeInBST(root.left, key)
        else:
            # root.val == key
            if root.left and root.right:
                l = root.left
                r = root.right
                while r.left and r.left.val > l.val:
                    r = r.left
                r.left = l
                root = root.right
            elif root.left and not root.right:
                root = root.left
            elif not root.left and root.right:
                root = root.right
            else:
                root = None
        return root

# Difficulty : Easy
# Category : Graph Traverse
# related problems: preorder, inorder, postorder
from collections import deque


class TreeNode:
    # Definition for a binary tree node
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.getLeftLeafNodes(root)
        return self.sum

    def getLeftLeafNodes(self, curNode: TreeNode):
        if not curNode:
            return

        if curNode.left and not curNode.left.left and not curNode.left.right:
            self.sum += curNode.left.val

        self.getLeftLeafNodes(curNode.left)
        self.getLeftLeafNodes(curNode.right)


if __name__ == '__main__':
    root = TreeNode(1)
    arr = [2, 3, None, 4, None, None, 6, 7, None, 8, None]
    queue = deque()
    queue.append(root)
    i = 0
    while queue:
        frontNode = queue.pop()
        if i < len(arr) and arr[i]:
            frontNode.left = TreeNode(arr[i])
            queue.append(frontNode.left)
        i += 1
        if i < len(arr) and arr[i]:
            frontNode.right = TreeNode(arr[i])
            queue.append(frontNode.right)
        i += 1

    #    1
    #   2 3
    #  4    6
    # 7    8
    # answer : 2
    s = Solution()
    print(s.sumOfLeftLeaves(root))

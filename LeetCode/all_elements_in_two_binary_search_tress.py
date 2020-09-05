# Definition for a binary tree node.
from typing import List
import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def inorder(node: TreeNode, lis: [int]):
            # 중위 순회 구현
            if not node:
                return

            inorder(node.left, lis)
            lis.append(node.val)
            inorder(node.right, lis)

        lis1 = []
        inorder(root1, lis1)
        lis2 = []
        inorder(root2, lis2)

        for num in lis2:
            # 이진 탐색(binary search) 이용해서 삽입
            insertPos = bisect.bisect_left(lis1, num)
            lis1.insert(insertPos, num)

        return lis1

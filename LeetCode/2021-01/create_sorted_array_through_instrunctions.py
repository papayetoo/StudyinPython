from typing import List
import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        # Key idea of the tree: at each node we record the number of values that got added
        # under and including this node so that at some node `u`, you can query `u.left.subtree_size`
        # to find out how many values added that are strictly less than `u` and `u.right.subtree_size`
        # for how may strictly less than `u`.
        self.subtree_size = 0
        # Since there are duplicate values in instructions, each node in the tree could
        # represent multiple instances of the same value added to the tree
        self.inst_cnt = 0


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def build_tree(values, first, last):
            if first > last:
                return None

            mid = (first + last) // 2
            # Since values is sorted, we can use the middle element as the subtree root
            # and ensure its left and right tree have equal number of elements. Or if you are
            # some maniac who got nothing better to do, you could implement an AVL tree or
            # Red-Black tree. Your choice!
            root = Node(values[mid])
            root.left = build_tree(values, first, mid - 1)
            root.right = build_tree(values, mid + 1, last)
            return root

        def mark_added(root, v):
            if v < root.val:
                mark_added(root.left, v)
            elif v > root.val:
                mark_added(root.right, v)
            else:
                root.inst_cnt += 1

            # This is a common pattern in augmented trees where we propogate the count of
            # of elements from the children up towards the root such that each time a
            # new element is added below the root of some subtree, we update at the root
            # the count so one could immediately query the size of the subtree without
            # exploring all the nodes of the subtree each time
            root.subtree_size += 1

        # Build a balanced tree using the list of sorted, unique values in instructions.
        # NOTE the elements merely form the tree, they aren't officially marked as added
        # until we call mark_added() that'd update `inst_cnt` and `subtree_size` for each
        # node to indicate that the value was indeed added
        values = sorted(collections.Counter(instructions).keys())
        root = build_tree(values, 0, len(values) - 1)

        p = 10 ** 9 + 7
        cost = 0
        for v in instructions:
            mark_added(root, v)

            # After the new value has been marked as added, it just a matter of traversing the
            # tree one more time until we reach `v` and note the `subtree_size` along the way
            # and add up how many values in the tree is either stricly less than `v` or greater than `v`
            curr = root
            nb_gt = 0
            nb_less = 0
            while v != curr.val:
                if v < curr.val:
                    nb_gt += (curr.right.subtree_size if curr.right != None else 0) + curr.inst_cnt
                    curr = curr.left
                elif v > curr.val:
                    nb_less += (curr.left.subtree_size if curr.left != None else 0) + curr.inst_cnt
                    curr = curr.right
            nb_less += curr.left.subtree_size if curr.left != None else 0
            nb_gt += curr.right.subtree_size if curr.right != None else 0
            cost = (cost % p + min(nb_gt, nb_less) % p) % p

        return cost % p
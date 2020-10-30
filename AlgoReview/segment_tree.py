import math


class SegmentTree:
    def __init__(self, arr: [int]):
        self.n = len(arr)
        self.arr = arr
        self.level = math.ceil(math.log2(self.n)) + 1
        self.tree = [0] * (2 ** (self.level) - 1)

    def buildSegmentTree(self, treeIndex: int, low: int, high: int):
        if low == high:
            self.tree[treeIndex] = self.arr[low]
            return

        mid = (low + high) // 2
        self.buildSegmentTree(2 * treeIndex + 1, low, mid)
        self.buildSegmentTree(2 * treeIndex + 2, mid + 1, high)

        self.tree[treeIndex] = self.tree[2 * treeIndex + 1] + self.tree[2 * treeIndex + 2]

    def querySegmentTree(self, treeIndex: int, low: int, high: int, i: int, j: int):

        if low > j or high < i:
            return 0

        if i <= low and j >= high:
            return self.tree[treeIndex]

        mid = low + (high - low) // 2
        if i > mid:
            return self.querySegmentTree(2 * treeIndex + 2, mid + 1, high, i, j)
        elif j <= mid:
            return self.querySegmentTree(2 * treeIndex + 1, low, mid, i, j)

        leftQuery = self.querySegmentTree(2 * treeIndex + 1, low, mid, i, mid)
        rightQuery = self.querySegmentTree(2 * treeIndex + 2, mid + 1, high, mid + 1, j)

        return leftQuery + rightQuery

    def updateSegmentTree(self, treeIndex: int, low: int, high: int, index: int, val: int):
        if low > index or high < index:
            return

        if low == high:
            self.arr[index] = val
            self.tree[treeIndex] = val
            return

        # mid = low + (high - low) // 2
        mid = (high + low) // 2
        self.updateSegmentTree(2 * treeIndex + 2, mid + 1, high, index, val)
        self.updateSegmentTree(2 * treeIndex + 1, low, mid, index, val)

        self.tree[treeIndex] = self.tree[2 * treeIndex + 1] + self.tree[2 * treeIndex + 2]


if __name__ == '__main__':
    #       0  1   2   3  4    5   6  7   8   9
    arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
    segtree = SegmentTree(arr)
    segtree.buildSegmentTree(0, 0, len(arr)-1)
    print(segtree.tree)
    # print(segtree.querySegmentTree(0, 0, len(arr)-1, 5, 7))
    segtree.updateSegmentTree(0, 0, len(arr)-1, 1, 20)
    print(segtree.tree)

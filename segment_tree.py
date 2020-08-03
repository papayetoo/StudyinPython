# 세그먼트 트리 구현 ----- 시간 초과 발생
import sys
import math
input = sys.stdin.readline()
N,M,K = map(int, input.rstrip().split())
arr = [0] * N
for i in range(N):
    arr[i] = int( sys.stdin.readline())
tree_height = math.ceil(math.log2(N)) + 1
tree_size = 1 << (tree_height + 1) - 1
tree = [0] * tree_size


def init(index, start, end):
    # bottom- up 방식
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start + end) // 2
        tree[index] = init(index*2+1, start, mid) + init(index*2 + 2, mid+1, end)
    return tree[index]


def getsum(node, start, end, left, right):
    # Top-down 방식
    if left > end or right < start:
        return 0

    if left <= start and end <= right :
        return tree[node]

    mid = (start + end) // 2
    return getsum(node*2 +1, start, mid, left, right) + getsum(node*2+2, mid+1, end, left, right)


def update(node, diff, index, start, end):
    # Top-down 방식
    # node 는 tree의 노드 번호
    # index 는 arr의 인덱
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end :
        mid = int(( start + end) / 2)
        update(node * 2 + 1, diff, index, start, mid)
        update(node * 2 + 2, diff, index, mid + 1, end)

init(0, 0, N-1)
result = []
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 1:
        diff = c - arr[b - 1]
        arr[b-1] = c
        update(0, diff, b - 1, 0, N -1)
    elif a == 2:
        result.append(getsum(0, 0, N-1, b - 1, c-1))

print(*result, sep='\n')


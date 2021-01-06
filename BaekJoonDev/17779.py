# 게리맨더링 2
from collections import defaultdict

def solution(n: int, r: int, c: int):
    grid = [[5 for _ in range(c)] for _ in range(r)]
    counter = defaultdict(int)

    for x in range(1, r + 1):
        for y in range(1, c + 1):
            for d1 in range(1, y):
                for d2 in range(1, n-y):

        def color(x, y, d1, d2):
            nonlocal grid
            grid[x][y]

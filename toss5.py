# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math
user_input = input()
k, n = user_input.split()
k = int(k)
n = int(n)
lst = [[0] * n for i in range(n)]

st_x = None
st_y = None
inc_x = [1, 0, -1, 0]
inc_y = [0, 1, 0, -1]
inc_idx = k - 1
if k == 1:
    st_x = 0
    st_y = 0
elif k == 2:
    st_x = n - 1
    st_y = 0
elif k == 3:
    st_x = n - 1
    st_y = n - 1
elif k == 4:
    st_x = 0
    st_y = n - 1

num = 1
for x in range(n):
    if k == 1:
        lst[st_y][st_x] = num
    elif k == 2:
        lst[st_y][st_x] = num
    elif k == 3:
        lst[st_y][st_x] = num
    elif k == 4:
        lst[st_y][st_x] = num
    num += 1
    if x != n - 1:
        st_x += inc_x[inc_idx]
        st_y += inc_y[inc_idx]

inc_idx += 1
for i in range(n - 1, -1, -1):
    for x in range(i):
        if 0 <= st_y + inc_y[inc_idx] <= n - 1 and 0 <= st_x + inc_x[inc_idx] <= n - 1:
            st_y += inc_y[inc_idx]
            st_x += inc_x[inc_idx]
            lst[st_y][st_x] = num
            num += 1
    inc_idx = (inc_idx + 1) % 4
    for x in range(i):
        if 0 <= st_y + inc_y[inc_idx] <= n - 1 and 0 <= st_x + inc_x[inc_idx] <= n - 1:
            st_y += inc_y[inc_idx]
            st_x += inc_x[inc_idx]
            lst[st_y][st_x] = num
            num += 1
    inc_idx = (inc_idx + 1) % 4

for r in lst:
    for c in r:
        print(' ' * (n -int(math.log10(int(c)))), c, sep='', end='')
    print()
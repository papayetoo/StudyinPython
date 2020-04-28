from itertools import combinations
def chickenDistance(chkzip, homes):
    ret = 0
    for h in homes:
        # print('home :', h[0] +1, h[1] +1)
        temp = 10**4
        for chk in chkzip:
            # print('chicken zip :', chk[0] +1, chk[1] +1)
            dist = abs(chk[0]-h[0]) + abs(chk[1]-h[1])
            temp = min(temp, dist)
        # print('chicken distance: {}'.format(temp))
        ret += temp
    return ret


n, number = map(int, input().split())
arr = [list( map( int, input().split() ) ) for _ in range(n)]
chickenzip = []
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chickenzip.append([i, j])
        if arr[i][j] == 1:
            home.append([i, j])
ans = 10**9
lst =  [i for i in range(len(chickenzip))]
comb = []
for i in range(1, number+1):
    tmp = list(combinations(chickenzip, i))
    comb += tmp
# print(comb)
for data in comb:
    dist = chickenDistance(data, home)
    ans = min(ans, dist)
print(ans)

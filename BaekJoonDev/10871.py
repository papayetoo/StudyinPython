N, X = [int(x) for x in input().split()]
arr = [a for a in input().split() if int(a) < X]
for a in arr:
    print(a, end=' ')
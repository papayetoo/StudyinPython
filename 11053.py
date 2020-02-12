n = input()
arr = list(map(int, input().split()))
dp = list(0 for i in range(int(n)))

for i in range(len(arr) - 1):
    dp[i] = 1
    max_value = arr[i]
    for j in range(i + 1, len(arr)):
        if (max_value < arr[j]):
            max_value = arr[j]
            dp[i] += 1

print(dp)
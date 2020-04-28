def addOneTwoThree(k = 0):
    dp = [0 for _ in range(0,11)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i - 3]

    return dp[k]

testCase = int(input())
answer = []
for i in range(testCase):
    answer.append(addOneTwoThree(int(input())))

for a in answer:
    print(a)
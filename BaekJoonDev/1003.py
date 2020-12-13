# 피보나치 수


if __name__ == "__main__":
    fib = [(0, 0) for _ in range(40)]
    fib[0] = (1, 0)
    fib[1] = (0, 1)
    for i in range(2, 40):
        fib[i] = (fib[i - 1][0] + fib[i - 2][0], fib[i - 1][1] + fib[i - 2][1])

    t = int(input())
    nums = [int(input()) for _ in range(t)]
    for n in nums:
        print(fib[n][0], fib[n][1])

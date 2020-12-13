# 피보나치 수
if __name__ == "__main__":
    fib = [0 for _ in range(21)]
    fib[0] = 0
    fib[1] = 1
    fib[2] = 1
    for i in range(3, 21):
        fib[i] = fib[i-1] + fib[i-2]

    n = int(input())
    print(fib[n])
import sys

if __name__ == '__main__':
    stdin = sys.stdin
    rows, cols = map(int, stdin.readline().split())
    arr = []
    for _ in range(rows):
        temp = list(map(int, stdin.readline().split()))
        arr.append(temp)
    print(arr)

    answer = 0
    for col in range(cols):
        i = 0
        start = arr[0][col]
        while i < rows:
            if abs(arr[i][col] - start) <= 1:
                i += 1
            else:
                break
        if i == rows:
            answer += 1
    print(answer)


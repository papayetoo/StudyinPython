# 자릿수 곱 문제
# 진수 변환

def solution(N):
    answer = []
    for i in range(2, 10):
        s = change(N, i)
        multResult = mult(s)
        answer.append([i, multResult])
    answer.sort(key=lambda x: (x[1], x[0]))
    return answer[-1]


def change(n: int, k: int):
    result = []
    while n > 1:
        result.insert(0, str(n % k))
        n //= k
    if n % k != 0:
        result.insert(0, str(n % k))
    return ''.join(result)


def mult(s: str):
    result = 1
    tmp = [int(x) for x in s if x != 0]
    for t in tmp:
        result *= t
    return result


if __name__ == "__main__":
    print(solution(14))
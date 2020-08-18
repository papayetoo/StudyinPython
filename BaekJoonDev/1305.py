# KMP 알고리즘 실패함수 이용하는 광고 문제
def get_pi(pat: str) -> int:
    pi = [0] * len(pat)
    i = 1
    j = 0

    while i < len(pat):
        if pat[i] == pat[j] :
            j += 1
            pi[i] = j
            i += 1
        else:
            if j != 0:
                j = pi[j-1]
            else:
                pi[j] = 0
                i += 1

    answer = []
    for i in range(1, len(pi)):
        answer.append( i - pi[i-1])
    return min(answer)


if __name__ == '__main__':
    pattern = 'aaaaaaa'
    print(get_pi(pattern))
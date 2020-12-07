# KMP 알고리즘 문제

def fail(pat: str):
    n = len(pat)
    ret = [-1] * n
    for i in range(1, n):
        j = ret[i - 1] + 1
        while j > 0 and pat[i] != pat[j]:
            j = ret[j - 1] + 1

        if pat[i] == pat[j]:
            ret[i] = j
        else:
            ret[i] = -1
    return ret

def kmp(s: str, p: str) -> bool:
    i = 0
    j = 0
    failure = fail(p)

    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = failure[j - 1] + 1
            else:
                j = 0
                i += 1

    return True if j == len(p) else False


if __name__ == '__main__':
    word = input()
    pattern = input()

    alphabets = [x for x in word if x.isalpha()]
    alphabets = ''.join(alphabets)
    print(1 if kmp(alphabets, pattern) else 0)
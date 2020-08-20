from typing import List


def fail(p: str) -> List[int]:
    pi = [-1] * len(p)
    for i in range(1, len(p)):
        j = pi[i - 1] + 1
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1] + 1

        if p[i] == p[j]:
            pi[i] = j
        else:
            pi[i] = -1

    return pi


def fail2(p:str) -> List[int]:
    pi = [-1] * len(p)
    i = 1
    j = 0
    while i < len(p):
        if p[i] == p[j]:
            pi[i] = pi[i-1] + 1
            i += 1
            j += 1
        else:
            if j == 0:
                pi[i] = -1
                i += 1
            else:
                j = pi[j-1] + 1
    return pi

def get_pi(p: str) -> List[int]:
    pi = [0] * len(p)
    i = 1
    # prefix 와 suffix가 동일한 길
    length = 0
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            pi[i] = length
            i += 1
        else:
            if length != 0:
                length = pi[length - 1]
            else:
                pi[i] = 0
                i += 1
    return pi


def kmp(s: str, p: str) -> bool:
    i = 0
    j = 0
    failure = fail(p)

    while i < len(s):
        print(s[i:], p[j:])

        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = failure[j - 1] + 1
            else:
                j = 0
                i = i + 1

        if j == len(p):
            return True

    return False


if __name__ == '__main__':
    m = 'cdefgabbabcabb'
    pattern = 'abb'
    print(fail2(pattern))
    print(kmp(m, pattern))

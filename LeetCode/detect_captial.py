import re
def solution(s: str):
    upper_count = 0
    lower_count = 0
    for c in s:
        if c.isupper():
            upper_count += 1
        else:
            lower_count += 1

    if upper_count == len(s):
        return True
    else:
        if lower_count == len(s):
            return True
        elif upper_count == 1 and s[0].isupper():
            return True
        else:
            return False


def solution2(word: str):
    flag = True if word[0].isupper() else False

    if flag is False:
        return True if word[1:].islower() else False
    else:
        return True if word[1:].islower() or word[1:].isupper() else False


def solution3(word: str):
    return True if re.fullmatch('[A-Z]*|.[a-z]*', word) is not None else False


if __name__ == '__main__':
    s = input()
    print(solution3(s))
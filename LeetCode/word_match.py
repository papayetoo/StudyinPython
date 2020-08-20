# 백준에서 본 문제인데 정답이라 확신할 수 없음.
from collections import deque
from string import ascii_uppercase

queue = deque()
vowel = 'AEIOU'


def dfs(word: [str], pos: int, vowel_count: int, n_vowel: int, output: str):
    if pos == len(word):
        if output.count('L') >= 1:
            print(output)
        return

    if word[pos] != '_':
        if word[pos] in vowel and vowel_count < 2:
            dfs(word, pos + 1, vowel_count + 1, 0, output + word[pos])
        elif word[pos] not in vowel and n_vowel < 2:
            dfs(word, pos + 1, 0, n_vowel + 1, output + word[pos])
    else:
        for c in ascii_uppercase:
            if c in vowel:
                if vowel_count < 2:
                    dfs(word, pos + 1, vowel_count + 1, 0, output + c)
                else:
                    continue
            else:
                if n_vowel < 2:
                    dfs(word, pos + 1, 0, n_vowel + 1, output + c)
                else:
                    continue


if __name__ == '__main__':
    word = input()
    word = [w for w in word]
    print(dfs(word, 0, 0, 0, ''))

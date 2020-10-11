from collections import defaultdict


def solution(k, score):
    diffDict = defaultdict(int)
    n = len(score)
    for i in range(n - 1):
        diff = score[i] - score[i + 1]
        diffDict[diff] += 1

    findHacked = [x for x in diffDict if diffDict[x] >= k]
    answer = []
    for i in range(n):
        front = score[i - 1] - score[i] if i - 1 >= 0 else -1
        back = score[i] - score[i + 1] if i + 1 < n else -1
        if front not in findHacked and back not in findHacked:
            answer.append(score[i])
    return len(answer)


if __name__ == '__main__':
    score = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]
    k = 2
    solution(k, score)

import itertools
T = int(input())
def combinations(arr, index, r):

    if index > len(arr):
        return

    if r == 0:
        for i in range(len(arr)):
            if i in visited:
                print(words[i], end=' ')
        print()
        return


    visited.append(index)
    combinations(arr, index+1, r-1)
    visited.pop()
    combinations(arr, index+1, r)


answer = [0] * T
for i in range(T):
    nword = int(input())
    words = []
    visited = []
    result = []
    for _ in range(nword):
        words.append(input())

    combinations(words, 0, 2)

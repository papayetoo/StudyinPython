def permutation(numbers:[int], r: int, depth:int):
    if r == depth:
        for i in range(0, r):
            print(numbers[i], end=' ')
        print()
        return

    for i in range(depth, len(numbers)):
        numbers[i], numbers[depth] = numbers[depth], numbers[i]
        permutation(numbers, r, depth+1 )
        numbers[i], numbers[depth] = numbers[depth], numbers[i]

def next_permutation(numbers:[int]):

    i = len(numbers) - 1
    while i >= 0 and numbers[i-1] >= numbers[i]:
        i -= 1
    i -= 1
    while i >= 0:
        j = i + 1
        while j < len(numbers) and numbers[i] < numbers[j]:
            j += 1
        numbers[j-1], numbers[i] = numbers[i], numbers[j-1]
        break
    numbers = numbers[:i+1] + numbers[i+1:][::-1]
    return numbers

if __name__ == '__main__':
    numbers = [i for i in range(1, 10)]
    numbers = [4,3,2,1]
    r = 3
    # permutation(numbers, r, 2)
    # print(next_permutation([4,3,2,1]))
    print(next_permutation([2,1,3,4]))
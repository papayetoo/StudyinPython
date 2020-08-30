def perm(nums: list, r: int, c: int):

    if r == c:
        for i in range(0, r):
            print(nums[i], end=' ')
        print()
        return

    for index in range(c, len(nums)):
        nums[index], nums[c] = nums[c], nums[index]
        perm(nums, r, c+1)
        nums[index], nums[c] = nums[c], nums[index]


visited = [False] * len(num)
def permutation(numbers=[], r = 0, depth = 0):
    if depth == r:
        for i in range(0, r):
            print(numbers[i], end=' ')
        print()
        return

    for i in range(depth, len(numbers)):
        numbers[i], numbers[depth] = numbers[depth], numbers[i]
        permutation(numbers, r, depth + 1)
        numbers[i], numbers[depth] = numbers[depth], numbers[i]


if __name__ == '__main__':
    numbers = [x for x in range(5)]
    # print(numbers)
    perm(numbers, 3, 0)
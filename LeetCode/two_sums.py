def twoSumsSolution(nums: [int], target: int):
    tb = {}
    for index, n in enumerate(nums):
        t = target - n
        tb[t] = index
    print(tb)
    tb = {key : value for key, value in tb.items() if key > 0}
    return tb.values()


if __name__ == '__main__':
    arr = [3, 2, 4]
    print(twoSumsSolution(arr, 6))

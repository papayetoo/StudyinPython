def removeDuplicate(num:[int]) -> int:

    cnt = 0
    prev = 0
    result = [num[prev]]
    for cur in range(1, len(num)):
        if num[prev] != num[cur]:
            result.append(num[cur])
        prev = cur

    return result

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicate(nums))

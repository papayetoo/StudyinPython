def heightChecker(heights:[int]) -> int:
    """
    :param heights:
    :return:
    """
    sorted_heights = sorted(heights)
    cnt = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            cnt +=1
    return cnt

heights = [5,1,2,3,4]
print(heightChecker(heights))

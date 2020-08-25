if __name__ == '__main__':
    s1 = 'def'
    s2 = 'dcefd'
    grid = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

    for r in range(len(s1)):
        for c in range(len(s2)):
            if s1[r] == s2[c]:
                if r - 1 >= 0 and c - 1 >= 0:
                    grid[r][c] = 1 + grid[r-1][c-1]
                else:
                    grid[r][c] = 1
            else:
                grid[r][c] = max(grid[r-1][c] if r - 1 >=0 else 0, grid[r][c-1] if c - 1 >=0  else 0)


    t = len(s1) - 1
    arr = grid[t]
    save_legnth = max(arr)
    lcs_length = max(arr)
    max_index = arr.index(lcs_length)
    res = []
    while lcs_length > 0:
        res.append(s2[max_index])
        t -= 1
        lcs_length -= 1
        max_index -= 1
        arr = grid[t]
        while lcs_length == arr[max_index] and max_index >= 0:
            max_index -= 1
        max_index += 1
        # max_index = arr.index(lcs_length)
    print(''.join(res[::-1]), save_legnth)
def combination(arr: [int], visited: [int], index: int, depth: int, target: int):
    if index > len(arr) or target < 0:
        return

    if depth == 0 and target == 0:
        for i in visited:
            print(arr[i], end=' ')
        print()
        return

    visited.append(index)
    if index < len(arr):
        combination(arr, visited, index + 1, depth - 1, target - arr[index])
    visited.pop()
    combination(arr, visited, index + 1, depth, target)


if __name__ == "__main__":
    arr = [x for x in range(1, 10)]
    combination(arr,[],  0, 3, 15)

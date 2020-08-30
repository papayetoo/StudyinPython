visited=[]
def combination(arr: list, index: int, depth: int):
    if index > len(arr):
        return

    if depth == 0:
        for i in visited:
            print(arr[i], end=' ')
        print()
        return

    visited.append(index)
    combination(arr, index + 1, depth - 1)
    visited.pop()
    combination(arr, index + 1, depth)


if __name__ == "__main__":
    arr = [x for x in range(3)]
    combination(arr, 0, 2)


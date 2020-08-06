# 알고리즘 풀이 방식이 이해가 잘 안됨.
def printReapeating(arr, size):
    # 배열에 있는 값들이 배열에서 등장한 인덱스가 됨.
    # (1, 1, 2) 이면 arr[abs(arr[0]-1)] 의 값을 arr[0] = -1
    # 두 번째 1을 만났을 때에는 arr[abs(arr[1]-1)] 즉 arr[0]의 값이 음수이므로 이미 만난 값 따라서
    # 정답 배열에 1을 넣으면 됨
    # arr[abs(arr[2]-1)] 의 값은 -2가 됨.
    # 요약 이미 만난 인덱스에 해당하는 값은 음수로 변해있음
    # 만나지 않은 인덱스는 음수로 변경.
    for i in range(size):

        if arr[abs(arr[i])-1] >= 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            print( abs(arr[i]), end=' ')
    print()
    print(arr)

if __name__ == '__main__':
    arr = [4,3,2,7,8,2,3,1]
    printReapeating(arr, len(arr))
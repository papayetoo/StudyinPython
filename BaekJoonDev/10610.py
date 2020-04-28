# 백준 10610 문제 30의 가장 큰 배수 만들기 문제
def sol10610():
    n = input()
    arr = [0 for _ in range(0, 10)] # 10^5까지 숫자가 주어질 수 있기 때문에 순열 구현은 안함. 매우 속도가 느림.
    # 대신에 카운팅 정렬 방식을 이용함. 여기서 매우 유용함.
    sum = 0

    for i in range(len(n)):
        intValue = int(n[i])
        arr[intValue] += 1
        sum += intValue

    if sum % 3 != 0 or arr[0] == 0 :
        print(-1)
        return

    result = ""
    for i in range(9,-1, -1):
        while arr[i] > 0:
            result += str(i)
            arr[i] -= 1
    print(result)
    return

sol10610()
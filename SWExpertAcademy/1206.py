# 1일차 view

case = []
for i in range(10):
    n = int(input())
    buildings = list(map(int, input().split()))

    index = 2
    cnt = 0
    while index < n - 2 :
        if buildings[index] > buildings[index+1] and buildings[index] > buildings[index - 1]:
            # 왼쪽에서 제일 높은 빌딩과 오른쪽에서 제일 높은 빌딩을 찾음
            lmax,rmax = max( buildings[index-2:index]), max(buildings[index+1:index+3])
            # 그 중에서 제일 높은 빌딩을 찾음.
            nearmax = max(lmax, rmax)
            # 제일 높은 빌딩과 현재 빌딩의 높이를 비교하고 현재 빌딩이 더 높다면 조망권이 확보된 세대수를 증가함.
            if nearmax < buildings[index]:
                cnt += buildings[index] - nearmax
        index += 1
    case.append(cnt)

for index, value in enumerate(case):
    print('#{} {}'.format(index+1, value))





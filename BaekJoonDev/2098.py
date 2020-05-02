import sys
sys.setrecursionlimit(10**9)
numOfCities = int(input())
dist =  [ list(map(int, sys.stdin.readline().split())) for _ in range(numOfCities)]
buffer = [ [ float('inf') for _ in range(2**numOfCities + 1)] for _ in range(numOfCities)]
dp = [ [0] * (1<<numOfCities) for _ in range(numOfCities)]

v = 1 << 0
INF = 1e30
def tsp(current, visited):

    # 시작 정점으로 돌아오는 부분.
    if visited ==(1 << numOfCities) -1:
        if dist[current][0] != 0:
            return dist[current][0]
        else:
            return INF

    # 메모이제이션을 위한 부분
    # 계산 시간 절감 위한 코드
    ret = buffer[current][visited]
    if ret != float('inf'):
        return ret

    ret = float('inf')
    for i in range(numOfCities):
        # dist[current][i]로 가는 길이 존재하고,
        # visited & (1 << i) 는 1이면 i를 방문한 적 있다는 의미 0이면 그 반대
        if dist[current][i] and  not visited&(1 << i):
            ret = min(ret , tsp(i, visited | (1 << i)) + dist[current][i])
    # 메모이제이션에서 연산 값을 저장하기 위한 부분.
    buffer[current][visited] = ret
    return ret

print(tsp(0, 1))

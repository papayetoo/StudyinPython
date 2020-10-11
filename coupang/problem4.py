from collections import defaultdict


def solution(depar, hub, dest, roads):
    # 방문 여부 확인
    visited = []
    # 그래프 생성 작업
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
    # 그래프 생성 완료
    answer = 0
    def dfs(curCity: str, path: list):
        nonlocal answer
        if curCity == dest and hub in path:
            answer += 1
            return
        for otherCity in graph[curCity]:
            if otherCity not in visited:
                visited.append(otherCity)
                path.append(otherCity)
                dfs(otherCity, path)
                path.pop()
                visited.pop()

    visited.append(depar)
    dfs(depar, [depar])
    return answer

if __name__ == '__main__':
    roads = [["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "DAEJEON"], ["SEOUL", "ULSAN"],
             ["DAEJEON", "DAEGU"], ["GWANGJU", "BUSAN"], ["DAEGU", "GWANGJU"], ["DAEGU", "BUSAN"], ["ULSAN", "DAEGU"],
             ["GWANGJU", "YEOSU"], ["BUSAN", "YEOSU"]]
    depar = 'SEOUL'
    hub = 'DAEGU'
    dest = 'YEOSU'
    # depar = 'ULSAN'
    # hub = 'SEOUL'
    # dest = 'BUSAN'
    # roads = [["SEOUL", "DAEJEON"], ["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "ULSAN"],
    #          ["DAEJEON", "BUSAN"], ["GWANGJU", "BUSAN"]]
    print(solution(depar, hub, dest, roads))

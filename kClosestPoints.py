def kClosest(points:list[list[int]], K:int)-> list[list[int]]:
    # first solution
    points.sort(key= lambda P: P[0]**2 + P[1]**2)
    return points[:K]

    # my solution
    # 딕셔너리로 저장한 후에 값에 의한 정렬후 K까지 출력
    # dist = {}
    # for p in points:
    #     dist[(p[0],p[1])] = p[0]**2 + p[1]**2
    # newlst = sorted(__iterable=dist, key= lambda k: dist[k])
    # return newlst[:K]

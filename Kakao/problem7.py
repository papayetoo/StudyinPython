def solution(sales, links):
    answer = 0
    parents = [i for i in range(0, len(sales) + 1)]
    sales.insert(0, 0)
    costs = {}
    for manager, worker in links:
        parents[worker] = manager

    def find(u: int):
        if u == parents[u]:
            return u
        return find(parents[u])

    def merge(u, v):
        u = find(u)
        v = find(v)

        if u == v:
            return min(sales[u], sales[v])

        if sales[u] > sales[v]:



    return answer



def merge(u: int, v: int, parents: [int]):
    u = find(u, parents)
    v = find(v, parents)

    if u == v:
        return



if __name__ == '__main__':
    sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    solution(sales, links)
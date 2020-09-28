from typing import List
import collections

class Solution:
    def __init__(self):
        self.res = []

    def calcEquation(self, eq: List[List[str]], val: List[float], q: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for i in range(len(eq)):
            graph[eq[i][0]].append([val[i], eq[i][1]])
            graph[eq[i][1]].append([1 / val[i], eq[i][0]])

        def dfs(start, end, graph, ans, vis):
            if start not in graph or end not in graph or start in vis:
                return -1
            if start == end:
                return ans
            vis.add(start)
            for weight, v in graph[start]:
                if v not in vis:
                    value = dfs(v, end, graph, ans * weight, vis)
                    if value != -1:
                        return value
            return -1

        for i in range(len(q)):
            start = q[i][0]
            dest = q[i][1]
            self.res.append(dfs(start, dest, graph, 1, set()))
        return self.res
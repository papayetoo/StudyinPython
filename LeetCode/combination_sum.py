from typing import List
from collections import defaultdict


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        visited = []
        answer = []

        #         def combination(current: int, res: List[int], i: int):
        #             if current < 0:
        #                 return

        #             if current == 0:
        #                 if len(visited) == 0 or set(res) not in visited:
        #                     tmp = []
        #                     tempCandidates = []
        #                     for i in res:
        #                         # print(candidates[i], end=' ')
        #                         tmp.append(i)
        #                         tempCandidates.append(candidates[i])
        #                     # print()
        #                     visited.append(tmp)
        #                     answer.append(tempCandidates)
        #                 return

        #             for i in range(n):
        #                 res.append(i)
        #                 combination(current-candidates[i], res, i + 1)
        #                 res.pop()
        def combination(current: int, res: defaultdict(int), i: int):
            if current < 0:
                return

            if current == 0:
                tmp = []
                for i in res:
                    tmp += [candidates[i]] * res[i]
                if tmp not in answer:
                    answer.append(tmp)
                return

            for i in range(n):
                res[i] += 1
                combination(current - candidates[i], res, i + 1)
                res[i] -= 1

        dic = defaultdict(int)
        combination(target, dic, 0)
        return answer
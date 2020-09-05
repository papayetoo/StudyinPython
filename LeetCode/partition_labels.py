from typing import List
class Solution:
    def partitionLabels(self, s:str) -> List[int]:
        last = {}
        for index, char in enumerate(s):
            # for saving last index of character
            last[char] = index
        print(last)
        def findLastIndex(sub: str, st: int, end:int):
            nMax = 0
            for char in sub:
                nMax = max(nMax, last[char])
            if nMax == end:
                return nMax
            else:
                return findLastIndex(s[st:nMax+1], st, nMax)

        i = 0
        ans = []
        while i < len(s):
            end = last[s[i]]
            sub = s[i:end+1]
            end = findLastIndex(sub, i, end)
            ans.append(len(s[i:end+1]))
            i = end + 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels('ababcbacadefegdehijhklij'))
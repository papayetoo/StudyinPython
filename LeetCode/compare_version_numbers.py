class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vOne = version1.split('.') + ['0'] * abs(len(version1) - len(version2))
        vTwo = version2.split('.') + ['0'] * abs(len(version1) - len(version2))
        l = 0
        s = 0
        while s < len(vOne) and l < len(vTwo):
            if int(vOne[s]) > int(vTwo[l]):
                return 1
            elif int(vOne[s]) < int(vTwo[l]):
                return -1
            else:
                s += 1
                l += 1
        return 0


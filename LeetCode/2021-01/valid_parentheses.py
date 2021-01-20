from collections import Counter


class Solution:
    def isValid(self, s: str) -> bool:
        stc = []
        counter = Counter(s)
        if counter['('] != counter[')'] or counter['['] != counter[']'] or counter['{'] != counter['}']:
            return False
        i = 0
        n = len(s)
        left = ['{', '[', '(']
        right = ['}', ']', ')']
        while i < n:
            if s[i] in left:
                stc.append(s[i])
                i += 1
                continue
            if not stc and s[i] in right:
                return False
            if right.index(s[i]) == left.index(stc[-1]):
                stc.pop()
                i += 1
                continue
            else:
                return False
        return True

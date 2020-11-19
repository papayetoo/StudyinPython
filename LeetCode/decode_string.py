class Solution:
    def decodeString(self, s: str) -> str:

        out = ''
        n = len(s)

        def decode(number: int, st: int):
            repeatingStr = ''
            while st < n and s[st] != ']':
                if s[st].isdigit() == False:
                    repeatingStr += s[st]
                    st += 1
                    continue
                else:
                    newNumber = ''
                    while s[st].isdigit():
                        newNumber += s[st]
                        st += 1
                    newRepeat, st = decode(int(newNumber), st + 1)
                    repeatingStr += newRepeat
                    continue
            return repeatingStr * number, st + 1

        i = 0
        while i < n:
            if s[i].isdigit() == False:
                out += s[i]
                i += 1
                continue
            else:
                number = ''
                while s[i].isdigit():
                    number += s[i]
                    i += 1
                nOut, i = decode(int(number), i + 1)
                out += nOut
                continue
        return out


if __name__ == "__main__":
    s = "3[a10[bc]]"
    sol = Solution()
    print(sol.decodeString(s))
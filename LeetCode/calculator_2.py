from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def helper(op: str, num1: int, num2: int):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                return num1 // num2

        # 들어가는 우선 순위
        inPriority = {'+': 0, '-': 0, '*': 1, '/': 1}
        # 나가는 우선 순위
        # outPriority = {'+': 1, '-': 1, '*': 0, '/': 0}

        nums = deque([])
        ops = deque([])
        i = 0
        n = len(s)
        while i < n:
            temp = ''
            if s[i] == ' ':
                i += 1
                continue
            if not s[i].isdigit():
                if not ops:
                    ops.append(s[i])
                    i += 1
                else:
                    if inPriority[ops[-1]] < inPriority[s[i]]:
                        ops.append(s[i])
                        i += 1
                    else:
                        while ops and inPriority[ops[-1]] >= inPriority[s[i]]:
                            op = ops.pop()
                            n2 = nums.pop()
                            n1 = nums.pop()
                            ans = helper(op, n1, n2)
                            nums.append(ans)
                        ops.append(s[i])
                        i += 1
                continue
            else:
                while i < n and s[i].isdigit():
                    temp += s[i]
                    i += 1
                nums.append(int(temp))
                continue
        while ops:
            op = ops.pop()
            n2 = nums.pop()
            n1 = nums.pop()
            ans = helper(op, n1, n2)
            nums.append(ans)
        print(nums[0])
        return nums[0]


if __name__ == '__main__':
    sol = Solution()
    # sol.calculate("1-1+1")
    # sol.calculate('3+5 / 2')
    sol.calculate('1*2-3/4+5*6-7*8+9/10')
    # sol.calculate('3/2')

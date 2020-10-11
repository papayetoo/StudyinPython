from string import ascii_lowercase


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {char: weight for weight, char in enumerate(s)}
        stack = []
        visited = set()

        for i, symbol in enumerate(s):
            if symbol in visited:
                continue

            while len(stack) !=0 and symbol < stack[-1] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(symbol)
            visited.add(symbol)

        return ''.join(stack)

if __name__ == '__main__':
    sol = Solution()
    # s = 'bcabc'
    s = "mitnlruhznjfyzmtmfnstsxwktxlboxutbic"
    answer = sol.removeDuplicateLetters(s)
    print(answer)

from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str ) -> str:
        counter = Counter(secret)
        a = []
        b = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                counter[guess[i]] -= 1
                a.append(i)

        for i in range(len(guess)):
            if i not in a and guess[i] in counter and counter[guess[i]] > 0:
                counter[guess[i]] -= 1
                b.append(i)
        return f'{len(a)}A{len(b)}B'


if __name__ == '__main__':
    s = Solution()
    secret = '1123'
    guess = '0123'
    print(s.getHint(secret, guess))

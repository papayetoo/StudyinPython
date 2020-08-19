class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        vowel = 'aeiouAEIOU'
        def proc(w:str)->str:
            if w[0] not in vowel:
                return w[1:] + w[0] + 'ma'
            else:
                return w + 'ma'

        return ' '.join([proc(word)+'a'*(index+1) for index, word in enumerate(words)])


if __name__ == '__main__':
    s = Solution()
    msg = 'I love to eat an apple'
    print(s.toGoatLatin(msg))
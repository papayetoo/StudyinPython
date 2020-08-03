class Solution:
    def is_palindrome(self, s: str) -> bool:
        alpha_str = ''
        for c in s:
            if c.isalnum():
                alpha_str += c.lower() if c.isalpha() else c

        if alpha_str == alpha_str[::-1]:
            return True
        else:
            return False
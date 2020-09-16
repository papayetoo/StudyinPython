class Solution(object):
    def findMaximumXOR(self, nums):

        trie = {}

        # ------------------------------

        def update_trie(x):
            # update trie with binary representation of x

            cur = trie
            for bit in format(x, '032b'):

                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]

            cur['value'] = x

            return

        # ------------------------------

        def best_match(x):
            # try to match with complement of x as much as possible

            # recall that for xor opertator
            # 1 xor 0 = 1
            # 0 xor 1 = 1
            # 0 xor 0 = 1 xor 1 = 0

            cur = trie
            for bit in format(x, '032b'):

                rev = '0' if bit == '1' else '1'
                if rev in cur:
                    cur = cur[rev]
                else:
                    cur = cur[bit]
            print(x, cur['value'])
            return cur['value']

        # ------------------------------

        for x in nums:
            update_trie(x)

        max_xor = 0
        for x in nums:
            # update global maximal xor result
            max_xor = max(max_xor, x ^ best_match(x))

        return max_xor


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximumXOR([8,10, 2]))
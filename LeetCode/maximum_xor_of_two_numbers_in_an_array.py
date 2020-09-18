from typing import List


class TrieNode:
    def __init__(self, val: str = None):
        self.val = val
        self.childNodes = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        curNode = self.root
        for bit in f'{num:032b}':
            if bit not in curNode.childNodes:
                curNode.childNodes[bit] = TrieNode(bit)
            curNode = curNode.childNodes[bit]
        curNode.isEnd = True

    def search(self, num: int) -> bool:
        numToBinary = self.toBinary(num)
        curNode = self.root
        for b in numToBinary:
            if b not in curNode.childNodes:
                return False
            curNode = curNode.childNodes[b]
        return True if curNode.isEnd else False

    def bestMatch(self, num: int):
        curNode = self.root
        result = ''
        for bit in f'{num:032b}':
            rev = None
            if bit == '0':
                rev = '1'
            else:
                rev = '0'
            if rev in curNode.childNodes:
                result += rev
                curNode = curNode.childNodes[rev]
            else:
                result += bit
                curNode = curNode.childNodes[bit]

        # print(int(result, 2))
        return int(result, 2)




class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        answer = 0
        for num in nums:
            result = trie.bestMatch(num)
            # print(f'reulst {result}')
            # print(num, result, num ^ result)
            answer = max(num ^ trie.bestMatch(num), answer)
        return answer



if __name__ == '__main__':
    s = Solution()
    arr = [8,10,2]
    arrSums = [0] * len(arr)
    print( 6 & 7)
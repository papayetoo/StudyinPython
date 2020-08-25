from typing import List
# Trie Datastructure
# reversed order Trie
# Difficulty: Hard
class TrieNode:
    def __init__(self, ch: str = ''):
        self.ch = ch
        self.childNodes = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.endWord = []

    def insert(self, word: str):
        cur = self.root
        word = word[::-1]
        for w in word:
            node = cur.childNodes.get(w, TrieNode(w))
            cur.childNodes[w] = node
            cur = node
        cur.isWord = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.words = words
        self.prefix = ''
        for w in words:
            self.trie.insert(w)

    def query(self, letter: str) -> bool:
        self.prefix += letter
        curNode = self.trie.root

        for ch in reversed(self.prefix):

            if ch not in curNode.childNodes:
                break
            curNode = curNode.childNodes[ch]

            if curNode.isWord:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
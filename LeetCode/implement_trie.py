class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.isWordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for ch in word:
            # Python dictionary method get() returns a value for the given key. If key is not available
            # returns default value None
            node = currNode.childNodes.get(ch, TrieNode())
            currNode.childNodes[ch] = node
            currNode = node

        currNode.isWordEnd = True

    def search(self, word:str) -> None:
        currNode = self.root
        for ch in word:
            node = currNode.childNodes.get(ch)
            if not node:
                return False
            currNode = node

        return currNode.isWordEnd

    def startswith(self, prefix:str) -> bool:
        currNode = self.root
        for ch in prefix:
            node = currNode.childNodes.get(ch)
            if not node:
                return False
            currNode = node
        return True
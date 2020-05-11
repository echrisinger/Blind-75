class TrieNode:
    def __init__(self, c, is_terminal):
        self.char = c
        self.children = [None]*26
        self.is_terminal = is_terminal

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('', False)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            index = self._indexChar(c)
            if not curr.children[index]:
                curr.children[index] = TrieNode(c, False)
            
            curr = curr.children[index]
        
        curr.is_terminal = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._getLastNode(word)
        return node and node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._getLastNode(prefix) and True
    
    def _getLastNode(self, prefix: str) -> TrieNode:
        curr = self.root
        for c in prefix:
            if not curr:
                break

            index = self._indexChar(c)
            curr = curr.children[index]
        
        return curr
        
    def _indexChar(self, char: str) -> int:
        return ord(char) - ord('a')
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Node:
    def __init__(self):
        self.is_word = False
        self.children = [None]*26
        
def _to_i(c):
    return ord('a') - ord(c)

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for c in word:
            idx = _to_i(c)
            if not curr.children[idx]:
                curr.children[idx] = Node()
            
            curr = curr.children[idx]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stk = []
        stk.append((0, self.root))
        
        while stk:
            idx, parent = stk.pop()
            if idx == len(word):
                if parent.is_word:
                    return True
                continue
            
            char = word[idx]
            if char == '.':
                for child in parent.children:
                    if child:
                        stk.append((idx+1, child))
            else:
                char_idx = _to_i(char)
                child = parent.children[char_idx]
                if child:
                    stk.append((idx+1, child))
                    
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

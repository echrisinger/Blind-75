class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table = [False]*(len(s)+1)
        table[0] = True
        for end in range(1,len(s)+1):
            for w in wordDict:
                w_l = len(w)
                start = end-w_l
                if start >= 0 and (start-1 == -1 or table[start]) and s[start:end] == w:
                    table[end] = True
                    break
                
        return table[-1]

#### Trie Soln ####
class TrieNode:
    count = 0
    
    def __init__(self, val):
        self.val = val
        self.id = self.count
        self.__class__.count += 1
        self.children = [None]*26
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def insert(self, word):
        curr = self.root
        for c in word:
            idx = _to_i(c)
            if not curr.children[idx]:
                curr.children[idx] = TrieNode(c)
            
            curr = curr.children[idx]
        curr.is_word = True

def _to_i(c):
    return ord(c) - ord('a')

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return not s
        elif not s:
            return True
        
        trie = Trie()
        for w in wordDict:
            trie.insert(w)
            
        table = [
            [None]*trie.root.__class__.count
            for _ in range(len(s))
        ]
        root = trie.root
        first_child = root.children[_to_i(s[0])]
        return self.helper(s, 0, first_child, trie.root, table)
    
    def helper(self, s: str, idx: int, curr: TrieNode, root: TrieNode, table: List[List[any]]) -> bool:
        if not curr:
            return False
        elif table[idx][curr.id] is not None:
            return table[idx][curr.id]
        elif idx == len(s)-1:
            table[idx][curr.id] = curr.is_word
            return curr.is_word
        
        res = False
        next_c = s[idx+1]
        child_idx = _to_i(next_c)
        child_node = curr.children[child_idx]
        res |= self.helper(s, idx+1, child_node, root, table)
        if curr.is_word:
            new_child = root.children[child_idx]
            res |= self.helper(s, idx+1, new_child, root, table)
            
        table[idx][curr.id] = res
        return res


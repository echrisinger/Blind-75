MOVES = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_idx = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, word_idx):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_word = True
        curr.word_idx = word_idx

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found = []
        trie = Trie()
        for i, w in enumerate(words):
            trie.insert(w, i)
            for r in range(len(board)):
                for c in range(len(board[0])):
                    self.backtrack(board, r, c, trie.root, found)
                    
        return [words[i] for i in found]
    
    def backtrack(self, board, r, c, parent, found):
        if not(0 <= r < len(board) and 0 <= c < len(board[0])):
            return
        
        char = board[r][c]
        if char not in parent.children:
            return
        
        curr = parent.children[char]
        if curr.is_word:
            found.append(curr.word_idx)
            curr.is_word = False
        
        tmp = board[r][c]
        board[r][c] = '#'
        for r_d, c_d in MOVES:
            self.backtrack(board, r+r_d, c+c_d, curr, found)
        board[r][c] = tmp

# Was using O(n) space, modified path storage to set board entry as '#'
# Solution is timing out, but practically speaking, the same as the ones
# in the answers.
# Time: O(4^maxlen(w)*n) as 4 moves for each character in a word=> 4^maxlen(w).
# Space: O(n+maxlen(w)*w) 

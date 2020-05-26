MOVES = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sources = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    sources.append((row, col))
                    
        for row, col in sources:
            if self.backtrack(row, col, set(), 0, word, board):
                return True
        
        return False
    
    def backtrack(self, row, col, seen, idx, word, board):
        if idx == len(word):
            return True
        elif (row, col) in seen or\
            not(0 <= row < len(board) and 0 <= col < len(board[0])) or\
            board[row][col] != word[idx]:
            return False
        
        res = False
        seen.add((row, col))
        for r_d, c_d in MOVES:
            n_r = row + r_d
            n_c = col + c_d
            
            if self.backtrack(n_r, n_c, seen, idx+1, word, board):
                return True
        
        seen.remove((row, col))
        return False

# O(n^2) time, O(n) space

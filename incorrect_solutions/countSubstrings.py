class Solution:
    # initial inclincation is either:

    # sliding window
    # dynamic programming
    
    # sliding window will not work
    # abacaba
    # window: aba => abac => c, would miss whole string
    
    # dynamic programming it is
    
    def countSubstrings(self, s: str) -> int:
        chars = list(s)
        table = [
            [0]*(len(chars)+1)
            for _ in range(len(chars))
        ]
        
        
        """
        [
            [0, 0]
            [0, 0]
        ]
        """
        for length in range(1, len(chars)+1): # 1..len(chars)
            for i in range(0, len(chars)): # 0..len(chars)-1
                j = i + length # 1..last_char
                if j > len(chars):
                    continue
                res = table[i][j-1] + 1
                if j - 1 != i and self.is_palindrome(chars, i, j):
                    res += 1
                
                table[i][j] = res
                print(chars[i:j])
                print(table[i][j])
                
        return table[0][len(chars)]
        
    def is_palindrome(self, chars, p1, p2):
        p2 -= 1
        # because we're indexing the string
        while p1 <= p2:
            if chars[p1] != chars[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True


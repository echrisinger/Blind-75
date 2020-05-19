class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        chars = {}
        start = 0
        max_length = -1
        for i, c in enumerate(s):
            if c in chars:
                start = max(start, chars[c]+1)
                
            chars[c] = i
            max_length = max(i - start + 1, max_length)
        
        return max_length
            


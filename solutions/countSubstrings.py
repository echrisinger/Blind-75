class Solution:
    # initial inclincation is either:

    # sliding window
    # dynamic programming
    
    # sliding window will not work
    # abacaba
    # window: aba => abac => c, would miss whole string
    
    # dynamic programming it is
    
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)*2):
            if i >= len(s):
                left = i % len(s)
                right = left + 1
            else:
                left = right = i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count

# O(n) time, O(1) space


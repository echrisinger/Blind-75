class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        longest_start, longest_end = 0, 0
        
        for i in range(2*len(s)):
            if i < len(s):
                start = end = i
            else:
                start = i % len(s)
                end = start+1
        
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start > longest_end - longest_start:
                    longest_end = end
                    longest_start = start

                start -= 1
                end += 1
            
        return s[longest_start:longest_end+1]


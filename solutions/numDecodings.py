class Solution:
    def numDecodings(self, s: str) -> int:
        prev = 1
        prev2 = None
        final_digits = range(0,7)
        for length in range(1, len(s)+1):
            last_idx = length - 1
            res = 0
            if s[last_idx] != '0':
                res += prev
            
            if last_idx >= 1 and (s[last_idx-1] == '1' or (s[last_idx-1] == '2' and int(s[last_idx]) in final_digits)):
                res += prev2
            
            prev2 = prev
            prev = res
        
        return prev
        
        

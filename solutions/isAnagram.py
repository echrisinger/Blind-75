class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        
        for c in s:
            i = ord('a') - ord(c)
            counts[i] += 1
            
        for c in t:
            i = ord('a') - ord(c)
            counts[i] -= 1
            
        return not any(counts)


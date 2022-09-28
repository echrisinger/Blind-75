# O(t+s) space & time

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = Counter(s)
        t_c = Counter(t)
        
        return s_c == t_c

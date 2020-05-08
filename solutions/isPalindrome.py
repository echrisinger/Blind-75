import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i1 = 0
        i2 = len(s) - 1
        
        alphanumeric_regex = re.compile('[A-Za-z0-9]')
        res = True
        while (i1 <= i2) and res: # parens not required
            if not alphanumeric_regex.match(s[i1]):
                i1 += 1
            elif not alphanumeric_regex.match(s[i2]):
                i2 -= 1
            else:
                res &= s[i1].lower() == s[i2].lower()
                i1 += 1
                i2 -= 1
        
        return res


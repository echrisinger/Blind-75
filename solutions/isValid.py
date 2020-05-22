PARENS = {
    '(':')',
    '{':'}',
    '[':']',
}

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in PARENS:
                stk.append(c)
            elif not stk or PARENS[stk.pop()] != c:
                return False
        
        return not len(stk)



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                opening = stack.pop()
                if not (
                    opening == '(' and
                    c == ')'
                ) or (
                    opening == '{' and
                    c == '}'
                ) or (
                    opening == '[' and
                    c == ']'
                ):
                    continue
                else:
                    return False
                
        return True
                     

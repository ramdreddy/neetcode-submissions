class Solution:
    def isValid(self, s: str) -> bool:
        ##every time we see a new closing parenthesis, the most recent one must be a matching open. 
        ## so we keep a stacking with all the closes, and if the newest open doesn't match, we return false or we pop
        stack = []
        p = {'[':']', '{':'}', '(':')'}
        for c in s:
            if c in p:
                stack.append(c)
            else:
                if stack and c == p[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
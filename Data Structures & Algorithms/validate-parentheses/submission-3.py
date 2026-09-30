class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ## if it exists and matches top, pop: else pop. 
        checker = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in checker:
                if stack and stack[-1] == checker[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return (len(stack) == 0)
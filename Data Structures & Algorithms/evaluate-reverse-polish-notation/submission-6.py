
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        nstack = []
        for c in tokens:
            if c == '+':
                first = nstack[-1]
                nstack.pop()
                second = nstack[-1]
                nstack.pop()
                nstack.append(first + second)
            elif c == '-':
                first = nstack[-1]
                nstack.pop()
                second = nstack[-1]
                nstack.pop()
                nstack.append(second - first)
            elif c == '*':
                first = nstack[-1]
                nstack.pop()
                second = nstack[-1]
                nstack.pop()
                nstack.append(first * second)
            elif c == '/':
                first = nstack[-1]
                nstack.pop()
                second = nstack[-1]
                nstack.pop()
                x = int(second/first)
                nstack.append(x)
            else:
                num = int(c)
                nstack.append(num)
        return nstack[-1]
        
                    
            
        
        
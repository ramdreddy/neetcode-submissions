class MinStack:
    
    def __init__(self):
        self.stack = []
        self.ms = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ms:
            self.ms.append(val)
        else:
            cmin = min(self.ms[-1], val)
            self.ms.append(cmin)


    def pop(self) -> None:
        self.stack.pop()
        self.ms.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ms[-1]
        
        

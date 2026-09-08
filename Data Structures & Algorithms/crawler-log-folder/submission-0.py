class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for s in logs:
            if s == './':
                continue
            elif s == '../':
                if counter == 0:
                    continue
                else:
                    counter-=1
            else:
                counter+=1
        return counter

        
        
        
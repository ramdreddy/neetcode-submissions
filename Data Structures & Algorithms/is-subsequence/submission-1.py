class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target = len(s)
        counter = 0
        if len(s) > len(t):
            return False
        index = 0
        for i in range(len(t)):
            if counter == target:
                return True
            elif s[index] == t[i]:
                counter+=1
                index+=1
        if counter == target:
            return True
        return False
            

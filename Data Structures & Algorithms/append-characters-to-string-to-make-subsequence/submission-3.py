class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        p = 0
        count = 0
        while(p < len(s) and i < len(t)):
            if s[p] == t[i]:
                count +=1
                p+=1
                i+=1
            else:
                p+=1
            
        return len(t)-count
##put length of word followed by hashtag
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l)+'#'+s
        return res
             
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i+=1
            length = int(length)
            substr = s[i+1:i+length+1]
            res.append(substr)
            i =i + length + 1
        return res
            
                
                

        

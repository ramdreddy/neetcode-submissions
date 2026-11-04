##put num and then #

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

##
    def decode(self, s: str) -> List[str]:
        i = 0
        res =[]
        while i < len(s):
            lenstr = ""
            while i < len(s) and s[i] != '#':
                lenstr += s[i]
                i+=1
            strlen = int(lenstr)
            ad = s[i+1: i + 1 + strlen]
            res.append(ad)
            i = i + 1 + strlen
        return res


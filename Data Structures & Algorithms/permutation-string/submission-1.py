class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1)>len(s2)):
            return False
        freq1, freq2 = [0]*26, [0]*26
        #arrays init
        for r in range(len(s1)):
            freq1[ord(s1[r])- ord('a')]+=1 
            freq2[ord(s2[r])- ord('a')]+=1 
        matches = 0
        #matches init
        for i in range(26):
            if freq1[i] == freq2[i]:
                matches+=1
        l = 0
        r = len(s1)-1
        while(r < len(s2)):
            if(matches == 26):
                return True
            if(freq2[ord(s2[l])-ord('a')] == freq1[ord(s2[l])-ord('a')]):
                matches-=1
            freq2[ord(s2[l])-ord('a')]-=1
            if(freq2[ord(s2[l])-ord('a')] == freq1[ord(s2[l])-ord('a')]):
                matches+=1
            l+=1
            r+=1
            if(r < len(s2)):
                if(freq2[ord(s2[r])-ord('a')] == freq1[ord(s2[r])-ord('a')]):
                    matches-=1
                freq2[ord(s2[r])-ord('a')]+=1
                if(freq2[ord(s2[r])-ord('a')] == freq1[ord(s2[r])-ord('a')]):
                    matches+=1
        return False
        
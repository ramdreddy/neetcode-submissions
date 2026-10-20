class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0]*26
        l2 = [0]*26
        for c in s:
            l1[ord(c)-ord('a')]+=1
        for c in t:
            l2[ord(c)-ord('a')]+=1
        return l1 == l2

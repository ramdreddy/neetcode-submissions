class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker1 = [0]*26
        checker2 = [0]*26
        for c in s:
            checker1[ord(c)-ord('a')]+=1
        for c2 in t:
            checker2[ord(c2)-ord('a')]+=1
        return checker1 == checker2
        
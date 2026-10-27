###idea
###make a hash map of each anagram, linking an array to an array then print array for each key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        match = {}
        res = []
        for s in strs:
            ang = [0]*26
            for c in s:
                ang[ord(c)-ord('a')]+=1
            ang = tuple(ang)
            if ang in match:
                match[ang].append(s)
            else:
                match[ang] = []
                match[ang].append(s)
        for key in match:
            res.append(match[key])
        return res

                





        
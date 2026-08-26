class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        left2 = 0
        ans = ""
        while left < len(word1) and left2 < len(word2):
            ans += word1[left]
            ans += word2[left2]
            left+=1
            left2+=1
        if left == len(word1) and left2 == len(word2):
            return ans
        elif left == len(word1):
            add = word2[left2::]
            return ans+add
        else:
            add = word1[left::]
            return ans +add
        
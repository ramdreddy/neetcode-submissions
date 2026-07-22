class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mf = 0
        helper = {}
        ans = 0
        for r in range(len(s)):
            helper[s[r]] = 1 + helper.get(s[r], 0)
            mf = max(mf, helper[s[r]])
            while ((r-left+1)-mf) > k: 
                helper[s[left]]-=1
                left+=1
                
            ans = max(ans, r - left +1)
        return ans

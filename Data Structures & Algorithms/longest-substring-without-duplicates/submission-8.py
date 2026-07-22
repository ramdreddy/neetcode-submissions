class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set()
        left = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in tracker:
                tracker.remove(s[left])
                left+=1
            tracker.add(s[r])
            ans = max(ans, r - left +1)
        return ans
                
        
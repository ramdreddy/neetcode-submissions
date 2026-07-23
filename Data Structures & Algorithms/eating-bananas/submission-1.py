class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while (l <= r):
            ans = 0
            mid = (l+r)//2
            for i in piles:
                ans += (mid + i - 1)//mid
            if ans <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
            
        return res
        
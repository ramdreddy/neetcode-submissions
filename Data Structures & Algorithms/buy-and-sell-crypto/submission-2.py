class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = 0
        right = 1
        while(right < len(prices)):
            ans = max(ans, prices[right]-prices[left])
            if(prices[left] > prices[right]):
                left = right
                right+=1
            else:
                right+=1
        return ans
        
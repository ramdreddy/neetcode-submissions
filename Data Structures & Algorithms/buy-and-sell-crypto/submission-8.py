class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##start one ptr on each end
        ##while left is greater=right, move left
        ##move whichever next is greater
        ##
        ##
        ##
        left = 0
        right = 1
        res = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                res = max(res, prices[right]-prices[left])
                right+=1
            else:
                left = right
                right+=1
        return res
        
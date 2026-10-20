class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #start at 0,1
        ##if 1 > 0, 0 = 1
        buy = 0
        sell = 1
        res = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                res = max(res, prices[sell] - prices[buy])
            sell+=1
        return res

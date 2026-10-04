class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_array = [0] * len(prices)
        max_array[-1] = prices[-1]
        # compute and keep max from the right
        for i in range(len(prices)-2, -1, -1):
            max_array[i] = max(prices[i], max_array[i+1])

        # for each element check the max element on right and
        # compute the profit
        profit = 0
        for i in range(len(prices)-1):
            # profit = future sell - current buy
            profit = max(profit, (max_array[i+1] - prices[i]))
        
        return profit

        
        
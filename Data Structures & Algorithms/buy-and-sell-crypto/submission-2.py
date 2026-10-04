class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer solution
        # keep the pointer next to each other and continue

        max_p = 0
        buy, sell = 0, 1
        while sell < len(prices):
            # meaning loss, so i have better buy
            if prices[sell] < prices[buy]:
                # use this as buy option as its less
                buy = sell
            else:
                cp = prices[sell] - prices[buy]
                max_p = max(cp, max_p)

            # sell should always increment in a loop
            sell += 1
        
        return max_p

        
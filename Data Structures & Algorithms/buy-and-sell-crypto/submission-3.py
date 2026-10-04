class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP solution, optimal
        # here just keep track of min-buy, and compute profit thats it

        max_p = 0
        min_buy = prices[0]

        for each in prices:
            # always keep track of minimum buy that's possible
            min_buy = min(each, min_buy)
            # each is sell here and check best sell for min-buy
            max_p = max(max_p, (each - min_buy))
        return max_p
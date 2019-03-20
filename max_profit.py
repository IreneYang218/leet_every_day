def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i, p in enumerate(prices[:-1]):
        #     max_now = max(prices[i+1:])-p
        #     max_profit = max(max_now, max_profit)
        # return max_profit
        max_profit = 0
        if len(prices)==0:
            return 0
        min_price = prices[0]
        for p in prices:
            if p < min_price:
                min_price = p
            max_profit = max(max_profit, p-min_price) # max profit before and the today's price - previous min
        return max_profit
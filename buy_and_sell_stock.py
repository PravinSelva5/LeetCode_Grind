'''
Sucess, Passed all the test classes ... 136ms , faster than 7.32%
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minimum_buy = 10000
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum_buy:
                minimum_buy = prices[i]
            elif prices[i] - minimum_buy > max_profit:
                max_profit = prices[i] - minimum_buy
        return max_profit
        
'''
Another Successful code entry ... 124ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        max_profit = 0
        min_buy = 10000
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price - min_buy)
        return max_profit
'''
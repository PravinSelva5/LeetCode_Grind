'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

-------
RESULTS
-------
Time Complexity: O(N)
Space Complexity: O(1)

Runtime: 64 ms, faster than 52.70% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 15 MB, less than 70.66% of Python3 online submissions for Best Time to Buy and Sell Stock.

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         
            buyPrice = 10000
            profit = 0
            
            for price in prices:
                
                if buyPrice > price:
                    buyPrice = price
                
                else:
                    profit = max(profit, price - buyPrice)
            
            
            return profit
'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

--------
RESULTS
--------
Runtime: 1244 ms, faster than 64.47% of Python3 online submissions for Coin Change.
Memory Usage: 14.4 MB, less than 56.43% of Python3 online submissions for Coin Change.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount <= 0:
            return 0
        
        if min(coins) > amount:
            return -1
        
        DynamicArray = [10000] * (amount+1)
        DynamicArray[0] = 0
        
        for i in range(1, amount+1):
            
            for coin in coins:
                
                if coin <= i:
                    DynamicArray[i] = min(DynamicArray[i-coin] + 1, DynamicArray[i])
                
        return DynamicArray[amount] if DynamicArray[amount] != 10000 else  -1
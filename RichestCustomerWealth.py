'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Runtime: 48 ms, faster than 94.94% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.4 MB, less than 28.96% of Python3 online submissions for Richest Customer Wealth.
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_wealth = 0
        temp = 0
        
        for account in accounts:
            
            for wealth in account:
                
                temp += wealth
            
            max_wealth = max(max_wealth, temp)
            temp = 0
        
        return max_wealth
        
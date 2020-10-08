'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".


Submission 1:
Runtime: 32 ms, faster than 45.57% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 14.2 MB, less than 5.05% of Python3 online submissions for Defanging an IP Address.

'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        '''
        set a varibale equal to [.]
        Iterate through given string
            If current letter equals .
                replace it with saved var
        
        return address
        '''
        
        
        defanged_IP = ""
        anchor = 0
        
        for alpha in range(len(address)):
            
            if address[alpha] == '.':
                
                defanged_IP += address[anchor:alpha] + '[.]'
                anchor = alpha + 1
            
        defanged_IP += address[anchor:]
        
        return defanged_IP
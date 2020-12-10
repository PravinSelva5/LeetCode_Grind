'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

--------------
   RESULTS
--------------
Runtime: 68 ms, faster than 73.67% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.2 MB, less than 30.52% of Python3 online submissions for Add Two Numbers.


Time Complexity: O(N)
Space Complexity: O(N)
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        answer = ListNode(0)
        pointer = answer
        
        carry = total = 0
        
        while l1 or l2:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = int(total // 10)
            
            pointer.next = ListNode(total % 10)
            
            pointer = pointer.next
            
        if carry > 0:
            pointer.next = ListNode(carry)
        
        return answer.next
    

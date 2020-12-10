'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

BECASUE THE GIVEN LIST IS SINGLY-LINKED, THE HARDEST PART OF THIS QUESTION, IS FIGURING OUT WHICH NODE IS THE Nth ONE THAT NEEDS TO BE REMOVED


--------
RESULTS
--------
Time Complexity: O(N)
Space Complexity: O(1)

Runtime: 36 ms, faster than 41.26% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.3 MB, less than 18.59% of Python3 online submissions for Remove Nth Node From End of List.
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        behind_ptr = ListNode(0)
        answer = behind_ptr
        ahead_ptr = head
        
        behind_ptr.next = head
        
        for i in range(1, n+1):
            ahead_ptr = ahead_ptr.next
        
        while ahead_ptr != None:
            
            behind_ptr = behind_ptr.next
            ahead_ptr = ahead_ptr.next
        
        behind_ptr.next = behind_ptr.next.next
        
        return answer.next
            
            
            
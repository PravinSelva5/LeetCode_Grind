'''
Reverse a singly linked list.

Time Complexity: O(N)
Space Complexity: O(1)

-------------
  RESULTS
-------------
Runtime: 36 ms, faster than 62.97% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 35.51% of Python3 online submissions for Reverse Linked List.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_ptr = None
        
        while head is not None:
            nextptr = head.next
            head.next = prev_ptr
            
            prev_ptr = head
            head = nextptr
        
        return prev_ptr
            
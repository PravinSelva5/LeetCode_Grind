'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Runtime: 40 ms, faster than 39.21% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.3 MB, less than 8.31% of Python3 online submissions for Merge Two Sorted Lists.

-----------------------
      COMPLEXITY 
-----------------------
Time Complexity: O(N)
Space Complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Utilize the fact that the lists are sorted
        
        current = ListNode(0)
        answer = current  # points to the beginning of our list
        
        while l1 and l2:
            
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            
            current = current.next
        
        # If one list still needs to be added
        
        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next
        
        while l2:
            current.next = l2
            l2 = l2.next
            current = current.next
            
       
        return answer.next
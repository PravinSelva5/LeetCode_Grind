'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.


--------------------
      RESULTS
--------------------
Runtime: 48 ms, faster than 67.00% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.1 MB, less than 73.41% of Python3 online submissions for Linked List Cycle.

Time Complexity: O(N)
Space Complexity: O(1)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
         
            # initialize two pointers that will loop the given list
            fast = head
            slow = head
            
            # Loop through given linked list
            while fast and slow and fast.next:
                slow = slow.next
                fast = fast.next.next
                
                # Eventually fast and slow will meet if there is a cycle
                if fast == slow:
                    return True
      
'''
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

----------
 RESULTS
---------
 Time Complexity: O(N)
 Space Complexity: O(N)

Runtime: 40 ms, faster than 79.22% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 16.2 MB, less than 32.46% of Python3 online submissions for Odd Even Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        # pointers
        odd = head
        even = odd.next
        evenList = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        odd.next = evenList
    
        return head
        
        
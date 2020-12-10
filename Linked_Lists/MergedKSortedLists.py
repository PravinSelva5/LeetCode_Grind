'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

----------
 RESULTS
----------
Time Complexity: O(N^2)
Space Complexity: O(1)

Runtime: 112 ms, faster than 52.99% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.7 MB, less than 58.62% of Python3 online submissions for Merge k Sorted Lists.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        cur = ListNode(0)
        answer = cur

        while l1 and l2:
            
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            
            cur = cur.next
        
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
            
        return answer.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if len(lists) == 0:
            return None
        
        # pointers 
        i = 0
        last = len(lists) - 1
        j = last
        
        # main loop
        while last != 0:
            i = 0
            j = last
            
            # inner loop, will sort and merge two lists
            while j > i:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j
            
        return lists[0]
        
        
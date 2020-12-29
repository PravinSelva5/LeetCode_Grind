'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

-----------------
     RESULT
-----------------
Time Complexity: O(N)
Space Complexity: O(N), due to the recursive call stack

Runtime: 56 ms, faster than 34.48% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 17.9 MB, less than 60.37% of Python3 online submissions for Kth Smallest Element in a BST.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node):
        if node == None:
            return
        
        self.inOrder(node.left)
        
        self.k -= 1
        
        if self.k == 0:
            self.answer = node.val
            return 
        
        self.inOrder(node.right)
        
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Binary Search Trees already have a sorting algorithm built into them. They left subtree will be less than the part & right subtree will be greater than its parent
        self.k = k
        self.answer = None
        
        self.inOrder(root)
        
        return self.answer
        
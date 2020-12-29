'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

---------------
   RESULTS
---------------
Time Complexity: O(N)
Space Complexity: O(N)

Runtime: 68 ms, faster than 83.66% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 25.2 MB, less than 63.97% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == None:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if (left == None) and (right == None):
            return None
        
        if left != None and right != None:
            return root
        
        # 
        if left == None:
            return right
        
        if right == None:
            return left
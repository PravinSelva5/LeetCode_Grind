'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node


--------------------
    RESULTS
--------------------
Time Complexity: O(N)
Space Complexity: O(H), H represents the height of the tree

Runtime: 32 ms, faster than 97.68% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.2 MB, less than 33.21% of Python3 online submissions for Maximum Depth of Binary Tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        
        return max(left, right) + 1
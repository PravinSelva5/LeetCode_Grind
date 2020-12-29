'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

-------------------
Results
-------------------
Time Complexity: O(N)
Space Complexity: O(N)

Runtime: 44 ms, faster than 55.80% of Python3 online submissions for Path Sum.
Memory Usage: 15.9 MB, less than 34.85% of Python3 online submissions for Path Sum.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Sum(self,root, target, current):
        
        if root == None:
            return False
        
        current += root.val
        
        if current == target and (root.left == None and root.right == None):
            return True
        
        return (self.Sum(root.right, target, current) or self.Sum(root.left, target, current))
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.Sum(root, sum, 0)
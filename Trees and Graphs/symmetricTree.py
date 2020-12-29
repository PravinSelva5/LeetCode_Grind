'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

-------------------
Results
-------------------

Time Complexity: O(N)
Space Complexity: O(N)

Runtime: 28 ms, faster than 93.85% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.4 MB, less than 52.06% of Python3 online submissions for Symmetric Tree.


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isMirror(self,node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False
        
        return (node1.val == node2.val) and (self.isMirror(node1.left, node2.right)) and (self.isMirror(node1.right, node2.left))
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        return self.isMirror(root, root)
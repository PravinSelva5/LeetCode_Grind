'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

-----------
 RESULTS
----------
Time Complexity and Space Complexity are both O(N)


Runtime: 20 ms, faster than 99.06% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 14.2 MB, less than 58.36% of Python3 online submissions for Binary Tree Postorder Traversal.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Post order means, you check the left and right subtrees of a root before printing the root value
        
        if not root:
            return 
        
        answer = []
        # call stack
        s1 = []
        
        # stack that contains nodes that will be pushed to answer stack
        s2 =[]
        
        s1.append(root)
        
        while s1:
            
            x = s1[-1]
            s1.pop()
            s2.append(x)
            
            if x.left:
                s1.append(x.left)
            
            if x.right:
                s1.append(x.right)
        
        while s2:
            y = s2[-1]
            s2.pop()
            answer.append(y.val)
        
        return answer
            
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

---------
RESULTS
---------
Runtime: 32 ms, faster than 81.01% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.5 MB, less than 68.30% of Python3 online submissions for Binary Tree Level Order Traversal.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # When you see level by level, automatically think of Breadth First Search
        answer = []
        
        if root == None:
            return answer
        
        queue = [root]
        
        while queue:
            length = len(queue)
            temp = []
            
            for i in range(length):

                front = queue.pop(0)
                temp.append(front.val)

                
                if front.left != None:
                    queue.append(front.left)
                
                if front.right != None:
                    queue.append(front.right)
                
            answer.append(temp)
            temp = []
                
        
        return answer     
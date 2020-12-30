'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

---------
RESULTS
---------
Runtime: 32 ms, faster than 67.89% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.5 MB, less than 51.65% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        answer = []
        queue = collections.deque()
        
        zigzag = False
        queue.append(root)
        
        while queue:
            level = []
            for i in range(len(queue)):
                if zigzag:
                    node = queue.pop()
                    level.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                
                else:
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            answer.append(level)
            zigzag = not zigzag
        
        return answer
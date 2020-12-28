'''
----------------------------
 Binary Tree Implementation
----------------------------

# 7 becomes left child of 5
#		           4
#		       /       \
#		      5	        6
#	      /  \      /   \
#      7   None  None  None
#     / \
#  None  None

'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

'''
IN-ORDER TRAVERSAL: the left node gets visited, root node, then right node
'''
def inOrderTraversal(node):

    if node != None:
        inOrderTraversal(node.left)
        print(node.data)
        inOrderTraversal(node.right)

'''
PRE-ORDER TRAVERSAL: Root/current node gets visited, then left node(s), then right node(s)
'''

def preorderTraversal(node):
    
    if node != None:
        print(node.data)
        preorderTraversal(node.left)
        preorderTraversal(node.right)

'''
PRE-ORDER TRAVERSAL: Root/current node gets visited, then left node(s), then right node(s)
'''


root   = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)

root.left = node_5
root.right = node_6
node_5.left = node_7

inOrderTraversal(root)
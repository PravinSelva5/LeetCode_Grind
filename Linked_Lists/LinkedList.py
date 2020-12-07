'''
-  A linked list is a linear data strucutre where its elements are not stored in contiguous order in memory unlike an array.
- Two types:
    - Singly Linked List
    - Doubly Linked List
- Singly Linked List:
    -  nodes only have a pointer to the NEXT ELEMENT
    - first node in the linked list is called the HEAD
    - last node in the linked lis is called the TAIL
    - Disadvantages: O(n) searching
    - Advantages: Insertion and deletion are cheaper ( compared to arrays )
'''

# ----------------------------------- #
# ----------------------------------- #
#  Singly Linked List Implementation  #
# ----------------------------------- #
# ----------------------------------- #

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        linked_list =  ""
        while (temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)
    
    def insertNode(self, val, pos):
        




# Node structure to be: 5 => 1 => 3 => 7

linked_list =LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.printList()
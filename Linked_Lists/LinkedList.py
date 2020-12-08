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
    
    # lists starts at 0
    def insertNode(self, val, pos):
        target = Node(val)
        if (pos == 0):
            target.next = self.head
            self.head = target
            return
        
        def getPrev(pos):
            temp = self.head
            count = 1
            while count < pos:
                temp = temp.next
                count += 1
            return temp
        
        prev = getPrev(pos)
        nextNode = prev.next

        prev.next = target
        target.next = nextNode
    
    def deleteNode(self, key):
        temp = self.head

        if (temp is None):
            return
        
        if (temp.data == key):
            self.head = temp.next
            temp = None
            return
        
        while (temp.next.data != key):
            temp = temp.next
        
        target_node = temp.next
        temp.next = target_node.next
        target_node = None


#----------------------------------------------------#
#----------------------------------------------------#
#               DOUBLY LINKED LIST
#----------------------------------------------------#
#----------------------------------------------------#

'''
- A doubly linked list node has pointers to both the previous and the next nodes
- Insertion: 4 pointers need to be taken care of 
- Deletion: similar to insertion
'''

class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def createList(self, arr):
        start = self.head
        l = len(arr)

        temp = start
        pointer = 0

        while pointer < l:
            newNode = DoublyLinkedListNode(arr[pointer])
            if pointer == 0:
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            pointer += 1
        
        self.head = start
        return start
    
    def printList(self):
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        
        print(linked_list)
    
    def countList(self):
        temp = self.head
        count = 0
        while ( temp is not None ):
            temp = temp.next
            count += 1
        return count

    # consider the index starts at 1
    def insertAtLocation(self, value, index):
        temp = self.head
        count = self.countList()

        if ( count + 1 < index ):
            return temp
        
        newNode = DoublyLinkedListNode(value)

        # Case when user wants to add a new node as the new head
        if ( index == 1 ):
            newNode.next = temp
            temp.prev = newNode
            self.head = newNode
            return self.head
        
        # If new node is going to be the last node in the linked list
        if ( index == count + 1):
            while (temp.next is not None):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            return self.head
        
        # General Case
        pointer = 1
        while ( pointer < index - 1):
            temp = temp.next
            pointer += 1
        
        nodeAtTarget = temp.next

        newNode.next = nodeAtTarget
        nodeAtTarget.prev = newNode

        temp.next = newNode
        newNode.prev = temp
        
        return self.head
    
    def deleteAtLocation(self, index):
        temp = self.head

        count = self.countList()

        if (count < index):
            return temp

    # Deleting the first node
        if index == 1:
            temp = temp.next
            self.head = temp

    # Deleting the last node
        if count == index:
            while temp.next is not None and temp.next.next is not None:
                temp = temp.next
                temp.next = None # deleted the last node
                return self.head
    
        pointer = 1
        while pointer < index - 1: 
            temp = temp.next
            pointer += 1
        
        prevNode = temp
        nodeAtTarget = temp.next
        nextNode = nodeAtTarget.next

        # connect previous node with next node, to remove target node out of the linked list
        nextNode.prev = prevNode
        prevNode.next = nextNode

        return self.head


# Node structure to be: 5 => 1 => 3 => 7

linked_list =LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.insertNode(2,2)
linked_list.deleteNode(3)
linked_list.printList()

# Doubly Linked List commands to check if class and methods work

array = [1,2,3,4,5]

Dlinkedlist = DoublyLinkedList()
Dlinkedlist.createList(array)
Dlinkedlist.printList()
Dlinkedlist.insertAtLocation(6,6)
Dlinkedlist.printList()
Dlinkedlist.deleteAtLocation(2)
Dlinkedlist.printList()

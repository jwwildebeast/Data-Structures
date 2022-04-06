""" This is just  simple implementation of the Linked List data structure in Python """

''' Classes '''

# Creating the Node class to hold the data
class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

# Creating the Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

''' Functions / Methods '''

# Append function
def append(self, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_nodeself.tail = new_node

# Prepend function
def prepend(self, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node

# Insert After function
def insert_after(self, current_node, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    elif current_node is self.tail:
        self.tail.next = new_node
        self.tail = new_node
    else:
        new_node.next = current_node.next
        current_node.next = new_node

# Remove After function
def remove_after(self, current_node):
    if (current_node == None) and (self.head != None):   # Special case, remove head
        succeeding_node = self.head.next
        self.head = succeeding_node
        if succeeding_node == None:                     # Remove last item
            self.tail = None
    elif current_node.next != None:
        succeeding_node = current_node.next.next
        current_node.next = succeeding_node
        if succeeding_node == None:                     # Remove tail
            self.tail = current_node
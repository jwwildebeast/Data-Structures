""" This is just  simple implementation of the Doubly-Linked List data structure in Python """

''' Classes '''

# Creating the Node class
class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

# Prepend function
def prepend(self, new_node):
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

# Insert After function
def insert_after(self, current_node, new_node):
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    elif current_node is self.tail:
        self.tail.next = next_node
        new_node.prev = self.tail
        self.tail = new_node
    else:
        successor_node = current_node.next
        new_node.next = successor_node
        new_node.prev = current_node
        current_node.next = new_node
        successor_node.prev = new_node

# Remove function
def remove(self, current_node):
    successor_node = current_node.next
    predecessor_node = current_node.prev
    if successor_node is not None:
        successor_node.prev = predecessor_node
    if predecessor_node is not None:
        predecessor_node.next = successor_node
    if current_node is self.head:
        self.head = successor_node
    if current_node is self.tail:
        self.tail = predecessor_node

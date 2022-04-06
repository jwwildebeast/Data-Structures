""" This is just  simple implementation of a Queue using a Linked List data structure in Python """


''' Classes '''
###################################################///Classes for the Linked List\\\###################################################

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

####################################################///Class for the Queue\\\################################################################

# Creating the Stack class
class Queue:
    def __init__(self):
        self.list = LinkedList()


''' Functions / Methods '''

###################################################///Functions for the Linked List\\\#################################################

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


###################################################///Functions for the Queue\\\####################################################

# Enqueue function
def enqueue(self, new_item):
    new_node = Node(new_item)           # Create a new node to hold the data

    self.list.append(new_node)       # Insert the node as the list tail (end of queue)


# Dequeue function
def dequeue(self):
    dequeued_item = self.list.head.data     # Copy data from the list's head node (queue's front node)

    self.list.remove_after(None)            # Remove list head

    return dequeued_item                      # Return dequeued_item
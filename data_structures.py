print("Implemented Data Structures Lib -- Python")

class LinkedList:

    head = None
    def __init__(self, root = None):
        # Linked List can be instantiated with a root node or without
        # No root node is the default
        if root != None:
            self.head = LinkedListNode(root)


    def appendNodeToTail(self, data):
        if self.head!= None:
            # Head node exists
            self.head.next = LinkedListNode(data)
        else:
            # Linked List is empty
            # Assign the data to the head
            self.head = LinkedListNode(data)


class LinkedListNode:

    def __init__(self, data, next = None):
        # Node is default created with no next node
        self.data = data    # instance variable unique to each instance
        self.next = next

x = LinkedList()
if x.head != None:
    print(x.head.data)
x.appendNodeToTail("test")
print(x.head.data)

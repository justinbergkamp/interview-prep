print("Implemented Data Structures Lib -- Python")
import unittest


class TestLinkedListMethods(unittest.TestCase):

    def test_getLength(self):
        linkedList = LinkedList()
        self.assertEqual(linkedList.getLength(), 0)
        linkedListNonEmpty = LinkedList("test")
        self.assertEqual(linkedListNonEmpty.getLength(), 1)

    def test_append(self):
        linkedList = LinkedList()
        length = 10
        for x in range(length):
            linkedList.appendNodeToTail(str(x))

        self.assertEqual(linkedList.getLength(), length)

        linkedList.appendNodeToTail("10")

        self.assertEqual(linkedList.getLength(), length+1)




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
            n = self.head
            while n.next != None:
                n = n.next
            n.next = LinkedListNode(data)
        else:
            # Linked List is empty
            # Assign the data to the head
            self.head = LinkedListNode(data)

    def printLinkedList(self, node):
        while(node.next != None):
            print(node.data)
            node = node.next
        print(node.data)

    def deleteNode(self, data):
        node = self.head
        while(node.next != None):
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next
        self.head = None

    def getLength(self):
        node = self.head
        count = 0
        if node:
            count = 1
        else:
            return count
        while(node.next != None):
            count +=1
            node = node.next
        return count



class LinkedListNode:

    def __init__(self, data, next = None):
        # Node is default created with no next node
        self.data = data    # instance variable unique to each instance
        self.next = next

linkedList = LinkedList()

for x in range(10):
    linkedList.appendNodeToTail(str(x))

linkedList.printLinkedList(linkedList.head)

linkedList.deleteNode(str(5))

linkedList.printLinkedList(linkedList.head)

unittest.main()

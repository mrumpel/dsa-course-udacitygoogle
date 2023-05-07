"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, head=None):
        h = Node(head)
        self.head = h
        self.tail = h

    def enqueue(self, new_element):
        if not self.head:
            h = Node(new_element)
            self.head = h
            self.tail = h
        else:
            t = self.tail
            self.tail = Node(new_element)
            t.next = self.tail

    def peek(self):
        return self.head.value

    def dequeue(self):
        h = self.head
        self.head = self.head.next
        return h.value
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
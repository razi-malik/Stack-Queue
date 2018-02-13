#!/usr/bin/env python

'''
Code for Queue

from collections import deque
q = deque()
q.append('eat')
q.append('sleep')
q.append('code')

>>> q
deque(['eat', 'sleep', 'code'])

>>> q.pop()
'code'
>>> q.pop()
'sleep'
>>> q.pop()
'eat'

>>> q.pop()
IndexError: "pop from an empty deque"

'''

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.queue.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[-1]

    def size(self):
        return len(self.queue)

qu = Queue()
print qu.isEmpty()
qu.enqueue("Rana")
qu.enqueue("Dila")
#print(qu.peek())
qu.enqueue(True)
print qu.size()
print qu.isEmpty()
qu.enqueue(8.4)
print qu.dequeue()
#print qu.dequeue()
print qu.size()
print 'The peek is: ', qu.peek()

#The queue is: enqueue --> [8.4, True, Dila, Rana] --> dequeue


q = Queue()
q.size()
q.isEmpty()
q.enqueue(8.4)
q.dequeue()
q.dequeue()
q.size()

# Using Python's list as a queue:

q = ["Eric", "John", "Michael"]
q.append("Terry")
q.append("Graham")

# Here the queue is: dequeue <-- ['Eric', 'John', 'Michael', 'Terry', 'Graham'] <-- Enqueue
print 'The current q: ', q

print q.pop(0)
print q.pop(0)
print 'The current q: ', q
















#!/usr/bin/env python

'''
Code for Stack

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]

'''

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

s=Stack()

print s.isEmpty()
s.push(4)
s.push('dog')
print s.peek()
s.push(True)
print s.size()
print s.isEmpty()
s.push(8.4)
print s.pop()
print s.pop()
print s.size()

'''
The stack: 

8.4	
True
dog
4

'''















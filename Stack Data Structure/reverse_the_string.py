"""
Find the hidden message by reversing a string using a stack
Template code is provided in the exercise files
"""


class Stack:
    """
    Stack
    """
    def __init__(self):
        """
        Initialize function
        """
        self.items = []

    def is_empty(self):
        """
        to check whether stack is empty
        """
        #return len(self.items) == 0
        return not self.items

    def push(self, item):
        """
        To push the data in the stack
        """
        self.items.append(item)

    def pop(self):
        """
        To remove and return the data from the stack
        """
        return self.items.pop()

    def peek(self):
        """
        To check the top data and return from the stack
        """
        return self.items[-1]

    def size(self):
        """
        to check the size of the stack
        """
        return len(self.items)

    def __str__(self):
        """
        Ito change the string retun of the stack
        """
        return str(self.items)


STRING1 = "gninreaL nIdekniL htiw tol a nreaL"
REVERSED_STRING = ""
s = Stack()
for s1 in STRING1:
    s.push(s1)

#print(s)
while not s.is_empty():
    REVERSED_STRING += s.pop()

print(REVERSED_STRING)

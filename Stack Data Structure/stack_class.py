# Using a class to represent a stack
# Learning push and pop
# Using a list allows others to user inset, remove, etc
# Last In, First Out (LIFO)
# Add item to top of stack: append()
# Retrieve item from top of stack: pop()
# Both happed from the top

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        #return len(self.items) == 0
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    s.push(4)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())


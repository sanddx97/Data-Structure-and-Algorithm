"""
Python Data Structure: Queue class
"""
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        """
        """
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    # Test 1
    # q = Queue()
    # print(q)
    # print(q.is_empty())
    # q.enqueue("A")
    # q.enqueue("B")
    # q.enqueue("c")
    # print(q)
    # print(q.is_empty())
    # print(q.dequeue())
    # print(q.peek())
    # print(q.size())
    # print(q)

    # Test 2
    q = Queue()
    q.enqueue("Learning")
    q.enqueue("with")
    q.dequeue()
    q.enqueue("Linked")
    q.enqueue("In")
    q.dequeue()
    print(q)

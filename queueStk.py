from collections import deque

# queue is a data structure
# uses FIFO approach

queue = deque()

queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue)

queue.popleft()
queue.popleft()
print(queue)

# stack is a data structure
# uses LIFO approach

stack = deque()

stack.appendleft("https://realpython.com/")
stack.appendleft("https://realpython.com/pandas-read-write-files/")
stack.appendleft("https://realpython.com/python-csv/")
print(stack)

stack.popleft()
stack.popleft()
print(stack)


# creating linked list

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data


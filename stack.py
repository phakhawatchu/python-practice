from linked_list import Node

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        curr = self.head
        self.head = self.head.next
        curr.next = None
        return curr

    def peak(self):
        return self.head

    def contains(self, key):
        curr = self.head
        while curr:
            if curr.data is key:
                return True
            curr = curr.next
        return False

    def __repr__(self):
        curr = self.head
        nodes = []
        while curr:
            if curr is self.head:
                nodes.append(f"[Peak: {curr.data}]")
            else:
                nodes.append(f"[{curr.data}]")
            curr = curr.next
        return " -> ".join(nodes)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.peak())
print(s)
print(s.contains(3))
print(s.contains(2))

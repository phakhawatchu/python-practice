from linked_list import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None and self.tail == None

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty(): 
            node.next = self.head
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        curr = self.head
        self.head = self.head.next
        curr.next = None
        return curr

    def __repr__(self):
        curr = self.head
        nodes = []
        while curr:
            if curr is self.head:
                nodes.append(f"[Head: {curr.data}]")
            elif curr is self.tail:
                nodes.append(f"[Tail: {curr.data}]")
            else:
                nodes.append(f"[{curr.data}]")
            curr = curr.next
        return " -> ".join(nodes)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
print(q.dequeue())
print(q)
q.enqueue(q.dequeue().data)
print(q)
q.enqueue(q.dequeue().data)
print(q)
q.dequeue()
q.dequeue()
print(q)
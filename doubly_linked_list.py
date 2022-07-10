class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"<Node data={self.data}>"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None and self.tail == None

    def add(self, data):
        node = Node(data)
        if self.is_empty(): 
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert(self, data, index):
        if index == 0:
            self.add(data)
        else:
            pos = 1
            curr = self.head
            while pos < index:
                curr = curr.next
                pos += 1
            node = Node(data)
            node.next = curr.next
            if curr is self.tail:
                self.tail = node
            else:
                curr.next.prev = node
            curr.next = node
            node.prev = curr


    def remove(self, key):
        curr = self.head
        if self.head.data == key:
            self.head = self.head.next
            self.head.prev = None
            curr.next = None
            return curr
        elif self.tail.data == key:
            curr = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            curr.prev = None
            return curr
        else:
            while curr:
                if curr.data == key:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr.prev = None
                    curr.next = None
                    return curr
                curr = curr.next
            return None


    def __repr__(self):
        curr = self.head
        nodes = []
        while curr:
            if curr is self.head:
                nodes.append(f"[Head: {curr.data}]")
            elif curr.next is None:
                nodes.append(f"[Tail: {curr.data}]")
            else:
                nodes.append(f"[{curr.data}]")
            curr = curr.next
        return " <-> ".join(nodes)

    def reverse(self):
        curr = self.tail
        nodes = []
        while curr:
            if curr is self.tail:
                nodes.append(f"[Tail: {curr.data}]")
            elif curr.prev is None:
                nodes.append(f"[Head: {curr.data}]")
            else:
                nodes.append(f"[{curr.data}]")
            curr = curr.prev
        return " <-> ".join(nodes)

l = DoublyLinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
print(l)
print(l.reverse())
l.insert(5,1)
print(l)
print(l.reverse())
l.insert(6,3)
print(l)
print(l.reverse())
l.insert(7,6)
print(l)
print(l.reverse())
l.remove(7)
print(l)
print(l.reverse())
l.remove(4)
print(l)
print(l.reverse())
print(l.remove(41))
l.remove(6)
print(l)
print(l.reverse())
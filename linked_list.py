class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node data={self.data}>"

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        curr = self.head
        size = 0
        while curr:
            curr = curr.next
            size += 1 
        return size

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, data, index):
        if index == 0:
            self.add(data)
        else:
            node = Node(data)
            curr = self.head
            pos = 1
            while pos < index:
                curr = curr.next
                pos += 1
            node.next = curr.next
            curr.next = node

    def remove(self, key):          
        curr = self.head
        if key == curr.data:
            self.head = self.head.next
            curr.next = None
            return curr
        else:
            prev = curr
            curr = curr.next
            while curr:
                if curr.data == key:
                    prev.next = curr.next
                    curr.next = None
                    return curr
                else:
                    prev = curr
                    curr = curr.next

    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return curr
            else:
                curr = curr.next
        return None

    def index(self, index):
        curr = self.head
        pos = 0
        while curr:
            if pos == index:
                return curr
            else:
                curr = curr.next
                pos += 1
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
        return " -> ".join(nodes)

# l = LinkedList()
# l.add(1)
# l.add(2)
# l.add(3)
# l.add(4)
# l.insert(5,1)
# l.insert(6,3)
# l.insert(7,5)
# l.remove(7)
# print(l)
# print(l.search(2))
# print(l.search(8))
# print(l.index(2))
# print(l.size())
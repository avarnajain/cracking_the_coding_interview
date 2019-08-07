class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return "<Node> {} next:{}".format(self.data, 
                                            self.next.data if self.next else self.next)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "<LinkedList> head:{}, tail:{}".format(self.head, 
                                                self.tail)

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def length(self):
        if not self.head:
            return 0
        elif not self.head.next:
            return 1
        count = 1
        current = self.head
        while current.next:
            count+=1
            current = current.next
        return count

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev

class DoubleNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __repr__(self):
        return "<DoubleNode> d:{} n:{} p:{}".format(self.data, 
                                                    self.next.data if self.next else self.next, 
                                                    self.prev.data if self.prev else self.prev)

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        return "<DoublyLinkedList> head:{} tail:{}".format(self.head, 
                                                    self.tail)

    def append(self, data):
        node = DoubleNode(data)
        if not self.head:
            self.head = node
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
        self.tail = node

    def remove(self, data):
        if self.head.data == data:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
            return 
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
                current.next.prev = current
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current)
            current = current.next
            
    def length(self):
        if not self.head:
            return 0
        elif not self.head.next:
            return 1
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    # def reverse(self):
    #     if self.head and self.tail:
    #         t = self.head
    #         t.prev = t.next
    #         t.next = None
    #         h = self.tail
    #         h.next = h.prev
    #         h.prev = None
    #         self.head = t
    #         self.tail = h
    #     return

print("----------2.1----------")

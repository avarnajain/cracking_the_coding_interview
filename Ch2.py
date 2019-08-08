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
                return current
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

#basic ll test case
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("----------2.1----------")
def rem_dups(ll):
    current = ll.head
    l = set()
    while current:
        if current.data in l:
            ll.remove(current.data)
        l.add(current.data)
        current = current.next
    return ll
def rem_dups_runner(ll):
    current = ll.head
    while current:
        runner = current.next
        while runner:
            if current.data == runner.data:
                ll.remove(runner.data)
            runner = runner.next
        current = current.next
    return ll
# ll.append(2)
# print(rem_dups(ll))
# ll.append(2)
# print(rem_dups_runner(ll))

print("----------2.2----------")
def kth_to_last_element(ll, k):
    if not ll.head:
        return 0
    index = ll.length() - k + 1
    count = 1
    current = ll.head
    while current:
        if count==index:
            return count
        count += 1
        current = current.next
    return 0
def kth_to_last_recursive(ll, k):
    if not ll.head:
        return 0
    index = ll.length() - k + 1
    print('index', index)
    kth = iterate_to_k(ll.head, index, i=1)
    return kth
def iterate_to_k(node, index, i):
    print('node', node, 'index', index, 'i', i)
    if i == index:
        return node
    if i > index or not node:
        return 0
    iterate_to_k(node.next, index, i+1)
# ll.append(6)
# print(kth_to_last_element(ll, 3))
# print(kth_to_last_element(ll, 1))
# print(kth_to_last_element(ll, 7))
# print(kth_to_last_recursive(ll, 3))
# print(kth_to_last_recursive(ll, 1))
# print(kth_to_last_recursive(ll, 7))

print("----------2.3----------")
def delete_input_node(node):
    if not node or not node.next:
        return False
    _next = node.next
    node.data = _next.data
    node.next = _next.next
    return True
# print(delete_input_node(ll.find(3)))

print("----------2.4----------")
def partition(ll, x):
    if not ll.head:
        return False
    lower = LinkedList()
    higher = LinkedList()
    current = ll.head
    while current:
        if current.data < x:
            lower.append(current.data)
        else:
            higher.append(current.data)
        current = current.next
    current = higher.head
    while current:
        lower.append(current.data)
        current = current.next
    return lower

ll = LinkedList()
ll.append(1)
ll.append(5)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(6)
print(partition(ll, 3))
print(partition(ll, 4))






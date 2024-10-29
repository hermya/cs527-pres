class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.last = None
    
    def addLeft(self, node: Node):
        if self.head == None:
            self.head = node
            self.last = node
        else:
            self.head.prev = node
            self.head.prev.next = self.head
            self.head = self.head.prev
    
    def removeLeft(self):
        if self.head == None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            node.next = None
            return node
    
    def addRight(self, node: Node):
        if self.head == None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last.next.prev = self.last
            self.last = self.last.next
    
    def removeNode(self, node: Node):
        if self.head == node:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.last = None
            node.next = None
            return node
        elif self.last == node:
            self.last = self.last.prev
            if self.last:
                self.last.next = None
            else:
                self.head = None
            node.prev = None
            return node
        else:
            temp1 = node.prev
            temp2 = node.next
            temp1.next = temp2
            temp2.prev = temp1
            node.prev = None
            node.next = None
            return node
    
    def print(self):
        if not self.head:
            print(None)
            return
        head = self.head
        print((head.value), end="")
        
        while head.next:
            head = head.next
            print(" ->", (head.value), end="")
        
        print()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
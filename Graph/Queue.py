class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None 

class Stack: 
    def __init__(self): 
        self.head = None 
    def isEmpty(self): 
        return self.head == None 
    def push(self, data): 
        n = Node(data)
        if self.isEmpty():
            self.head = n 
        else: 
            n.next = self.head 
            self.head = n 
    def pop(self):
        if self.isEmpty():
            return None
        data = self.head.data 
        self.head = self.head.next
        return data 
    def top(self): 
        return self.head.data
class Queue: 
    def __init__(self): 
        self.head = None 
        self.tail = None 

    def isEmpty(self): 
        return self.head == None 
    
    def Enqueue(self, data): 
        n = Node(data)
        if self.isEmpty(): 
            self.head = n
            self.tail = n
        else: 
            self.tail.next = n 
            self.tail = n 
    
    def Dequeue(self): 
        if self.isEmpty(): 
            return None 
        data = self.head.data 
        self.head = self.head.next
        return data
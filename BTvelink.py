# class Node: 
#     def __init__(self, data):
#         self.data = data
#         self.next = None 

#     def display(self):
#         print(f"{self.data}", end = " ")
# #end class

# class LinkList:
#     def __init__(self):
#         self.head = None 
#         self.tail = None 
    
#     def check(self, data): 
#         pass

#     def isEmpty(self): 
#         return self.head == None

#     def addFirst(self,data): 
#         if self.check(data): 
#             return 
#         node = Node(data)
#         if self.isEmpty(): 
#             self.head = self.tail = node 
#         else: 
#             node.next = self.head 
#             self.head = node 
    
    
#     def addLast(self, data): 
#         node = Node(data)
#         if self.isEmpty(): 
#             self.head = self.tail = node 
#         else: 
#             self.tail.next = node 
#             self.tail = node 

#     def display(self): 
#         cur = self.head
#         while cur: 
#             cur.display()
#             cur = cur.next
    
#     def delFirst(self):
#         if self.isEmpty(): 
#             return None
#         value = self.head.data
#         self.head = self.head.next
#         return value 
    
#     def delLast(self): 
#         if self.isEmpty(): 
#             return None 
#         cur = self.head 
#         while cur.next.next: 
#             cur = cur.next 
#         value = cur.next.data 
#         cur.next = None 
#         self.tail = cur 
#         return value
#     def delFirst(self): 
#         if self.isEmpty(): 
#             return None 
#         value = self.head.data
#         self.head = self.head.next 
#         return value
    
#     def addIndex(self, index, data):
#         if index < 0 :
#             return None 
#         if index == 0: 
#             self.addFirst(data)
#         cur = self.head 
#         pos = 0 
#         while cur: 
#             if pos + 1 == index: 
#                 break 
#             cur = cur.next 
#             pos += 1 
#         if cur == None: 
#             return 
#         if cur == self.tail:
#             self.addLast(data)
#         node = Node(data)
#         node.next = cur.next 
#         cur.next = node 
#     def delIndex(self, index): 
#         if index < 0: 
#             return None 
#         if index == 0: 
#             self.delFirst()
#         pos = 0 
#         cu = self.head 
#         while cu: 
#             if pos + 1 == index: 
#                 break 
#             pos += 1 
#             cu = cu.next 
#         if cu == None: 
#             return None 
#         if cu.next == None:
#             return None 
#         value = cu.next.data
#         cu.next = cu.next.data 
#         return value 




    

# myList = LinkList()
# myList.addFirst(6)
# myList.addFirst(7)
# myList.addFirst(8)
# myList.addLast(10)
# myList.addLast(11)
# # myList.delFirst()
# myList.delLast()
# myList.delFirst()
# myList.addIndex(2,50)
# myList.display()
# myList.delIndex(1)
# myList.display()



class Node: 
    def __init__(self, data): 
        self.next = None 
        self.data = data 
    
    def display(self): 
        print(f"{self.data}", end = " ")
#end class 
class LinkList: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
    
    def isEmpty(self): 
        return self.head == None 
    
    def addFirst(self, data): 
        node = Node(data)
        if self.isEmpty(): 
            self.head = self.tail = node
        
        else:
            node.next = self.head 
            self.head = node
    
    def addLast(self, data): 
        node = Node(data)
        if self.isEmpty(): 
            self.head = self.tail = node 
        else: 
            self.tail.next = node 
            self.tail = node 

    def display(self):
        cu = self.head 
        while cu: 
            cu.display()
            cu = cu.next

    def delFirst(self): 
        if self.isEmpty(): 
            return None 
        value = self.head.data 
        self.head = self.head.next
        return value
    
    def delLast(self): 
        if self.isEmpty():
            return None 
        cu = self.head 
        while cu.next: 
            cu.next = cu.next.next 
        value = self.head.data
        cu.next = self.tail 
        cu = self.tail 
        return value 
    

             
ML = LinkList()
ML.addFirst(5)
ML.addFirst(6)
ML.addFirst(7)
ML.addLast(8)
ML.addLast(9)
ML.addLast(10)
ML.delFirst()
ML.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    #end def
    def display(self):
        print(f"{self.data}", end = " ")
    
#end class
class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def check(self, data):
        #viet it nhat la 20 loai so khac nhau
        pass
        
    def isEmpty(self):
        return self.head == None
    
    def addFirst(self, data):
        if self.check(data):
            return
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
    def addIndex(self, index, data):
        if index < 0:
            return
        if index == 0:
            self.addFirst(data)
            return
        cur = self.head
        pos = 0
        while cur:
            if pos + 1 == index:
                break
            cur = cur.next
            pos+= 1 
        if cur == None: #index qua to
            return
        if cur == self.tail:
            self.addLast(data)
        node = Node(data)
        node.next = cur.next
        cur.next = node
        
    def display(self):
        cur = self.head
        while cur:
            cur.display()
            cur = cur.next
    
    def delFirst(self):
        if (self.isEmpty()): 
            return None 
        value = self.head.data
        self.head = self.head.next 
        return value
    
    def clear(self):
        self.head = None
    
    def delLast(self):
        if (self.isEmpty()):
            return None
        if (self.head == self.tail):
            value = self.head.data
            self.head = None 
            return value
        cu = self.head
        while cu.next.next:
            cu = cu.next
        value = cu.next.data # cu = self.tail.data
        cu.next = None
        self.tail = cu
        return value
    def delIndex(self, index):
        if (index<0):
            return None
        if (index == 0) :
            return self.delFirst()
        pos = 0
        cu = self.head
        while cu:
            if pos+1==index:
                break
            pos +=1
            cu = cu.next
        if cu == None:
            return None
        if cu.next == None: #cu = self.tail
            return None
        value = cu.next.data
        cu.next = cu.next.data
        return value 
#end class
# print(dir(int))
myList = Linklist()
myList.addFirst(1)
myList.addFirst(2)
myList.addFirst(3)
myList.addLast(10)
myList.addLast(20)
# myList.addLast(30)
# myList.addIndex(6,100)
# myList.addLast(1000)
#myList.clear()
# myList.addFirst(15)
# myList.display()
# myList.delIndex(5)
print("")
myList.display()



#UPDATE LIST:
#-Tăng giảm phần tử đầu tiên/cuối cùng(hoặc thứ k) lên 1 hoặc p đơn vị
#-Thay thế 1 hoặc là tất cả các phần tử một hamg nào đó tương ứng với giá trị tại vị trí đó
#-Thay thế tất cả các phần tử trong list bằng ước các số nguyên tố lớn nhất của nó
#-Bằng tổng các ước số của nó, không kể chính nó
#12 23 45 34 --> 16 1 32 
#-Reverse tất cả các phần từ thỏa mãn điều kiện abc(chẵn), còn các phần tử khác  thì đứng im.
#12 34 31 23 5 6 3 --> 6 34 31 23 5 12 3 
#-Thay thế các phần từ trong list bằng phần tử đối xứng của nó
# 21 43 13 32 5 6 3 
#-Sort tất cả các phần tử thỏa mãn điều kện abc(lẻ) theo thứ tự tăng dần, còn các phần từ khác đứng im
#12 34 31 23 5 6 3 --> 12 34 3 5 23 6 31 

# -------------------------
# class Node:
#     def __init__(self,data): 
#         self.data = data
#         self.next = None 
#     def display(self): 
#         print(f"{self.data}", end = " ")
# #end class 
# class LinkList: 
#     def __init__(self):
#         self.head = None 
#         self.tail = None 
#     def isEmpty(self): 
#         return self.head == None 
#     def addFirst(self, data): 
#         node = Node(data)
#         if self.isEmpty(): 
#             self.head == self.tail == node
#         node.next = self.head 
#         self.head = node 

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


# myList = LinkList()
# myList.addFirst(5)
# myList.addFirst(6)
# myList.addFirst(7)
# myList.addLast(8)
# myList.addLast(9)
# myList.display()
    



class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None 
        self.pre = None 

class DBLinkList: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.size = 0 
    
    def isEmpty(self): 
        # return self.head == None & self.tail == None 
        return self.size == 0 
    def addFirst(self, data): 
        node = Node(data)
        if self.isEmpty(): 
            self.head = node 
            self.tail = node
        else: 
            node.next = self.head 
            self.head.pre = node 
            self.head = node  
        self.size +=1 
    
    def display(self): 
        if (self.isEmpty()): 
            return 
        cu = self.head 
        while cu: 
            print(f"{cu.data}", end = " ")
            cu = cu.next 
        print("")
    
    # def reverseDisplay(self, data): 
    #     node = Node(data)
    #     if self.isEmpty(): 
    #         self.head = node 
    #         self.tail = node 
    #     else: 
    #         node.pre = self.head 
    #         self.head.next = node 
    #         self.head = node 
    #     self.size +=1 

    def addLast(self, data): 
        node = Node(data)
        if self.isEmpty(): 
            self.head = node 
            self.tail = node 
        else: 
            self.tail.next = node 
            node.pre = self.tail
            self.tail = node 
        self.size +=1 

    def addIndex(self, data, index): 
        if index < 0 or index > self.size: 
            return 
        if index == 0: 
            self.addFirst(data)
        elif index == self.size: 
            self.addLast(data)
        else: 
            node = Node(data)
            if index < self.size/2: 
                cu = self.head 
                pos = 0 
                while cu: 
                    if pos +1==index: 
                        break 
                    cu = cu.next 
                    pos+=1 
                node.next = cu.next 
                cu.next.pre = node 
                cu.next = node 
                node.pre = cu 
                self.size += 1 
            else: 
                cu = self.tail 
                pos = self.size-1
                while cu: 
                    if pos == index: 
                        break 
                    cu = cu.pre 
                    pos -=1
                cu.pre.next = node 
                node.pre = cu.pre 
                node.next = cu 
                cu.pre = node 
            self.size +=1 
    def delFirst(self): 
        if self.isEmpty(): 
            return
        else: 
            value = self.head.data
            self.head = self.head.next 
            self.head.pre = None 
            return value 
    
    # def delLast(self): 
    #     if self.isEmpty(): 
    #         return 
    #     if self.head == self.tail: 
    #         value = self.head.data 
    #         self.head = None 
    #         return value
    #     cu = self.head 
    #     while cu.next.next: 
    #         cu.next 
    #     value = cu.next.data 
    #     cu.next = None 
    #     self.tail = cu 
    #     return value

    def delIndex(self, index): 
        pass 
    def reverse(self): 
        pass 
    def sort(self, flag = True): #flag = True tang dan, flag = False giam dan) 
        pass
    def sort(self, flag = True): 
        i = self.head
        while i.next: #thuat toan interchange
            j = i.next 
            dc = False 
            while j: 
                # if flag and i.data > j.data: 
                #     dc = True 
                # if (not flag) and (i.data < j.data): 
                #     dc = True 
                if i.data > j.data == flag:
                    dc = True
                if dc: 
                    temp = i.data 
                    i.data = j.data 
                    j.data = temp
                j = j.next 
            i = i.next 
    
db = DBLinkList()
db.addFirst(1)
db.addFirst(2)
db.addFirst(3)
db.addFirst(4)
# db.reverse(5)
# db.reverse(6)
# db.reverse(7)
# db.reverse(8)
db.addLast(5)
db.addLast(6)
db.addIndex(10,4)
db.addIndex(20,3)
db.delFirst()
# db.delLast()
db.sort()
db.display()

# ----------------------
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.pre = None 
class DBLinkList: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.size = 0 
    def isEmpty(self): 
        return self.size == 0
    
    def addFirst(self, data): 
        node = Node(data)
        if self.isEmpty(): 
            self.head = node 
            self.tail = node 
        else: 
            node.next = self.head 
            self.head.pre = node 
            self.head = node 
        self.size +=1 
    
    def display(self): 
        if self.isEmpty():
            return 
        cu = self.head 
        while cu: 
            print(f"{cu.data}", end = " ")
            cu = cu.next 
        print("")

myList = DBLinkList()
myList.addFirst(5)
myList.addFirst(6)
myList.addFirst(7)
myList.display()

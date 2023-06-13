
#C1: delete by copying: 
# -Con trái:
#  +lấy giá trị ngoài cùng của con bên trái(của node cần xóa) copy lên vị trí cần xóa. Sau đó xía giá trị ngoài cùng bên phải của con bên trái (node này tối đa chỉ có 1 con)
# Trái - nghèo dốt, phải - giàu giỏi => chọn thằng giàu nhất của nhánh nghèo, copy lên 
# -Con phải: 
#  +Lấy giá trị ngoài cũng của con bên trái của con bê phải rồi copy lên vị trí cần xóa, sau đó xóa bỏ node ngoài cùng bên tría của con bên phải.
# Note: với delete by copying thì độ cao của cây là ko đổi hoặc chỉ có thể giảm tối đa là 1, phần lớn tất cả các vị trí trong cây là ko đổi.Chỉ có nốt mang đi copy ko đổi.
# C2: delete by Merging: 
# -Con trái: 
#  +lấy toàn bộ nhánh phải của node cần xóa rồi gán vào bên phải của node ngoài cùng bên phải của con trái(node cần xóa) sau đó tôn con trái lên làm cha.
# -Con phải: 
#  +lấy toàn bộ nhánh trái của node cần xóa rồi gán vào bên trái của node ngoài cùng bên trái của con phải(node cần xóa) sau đó tôn con phải lên làm cha.

#Uứng dụng của heap: trong sắp xếp và queue ưu tiên

from Node import *
class NodeQ: 
    def __init__(self, d): 
        self.d = d 
        self.next = None 
class MyQueue: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
    def isEmpty(self):
        return self.head == None
    def EnQueue(self, data): 
        n = NodeQ(data)
        if self.isEmpty(): 
            self.head = self.tail = n 
        else: 
            self.tail.next = n 
            self.tail = n 

    def DeQueue(self): 
        if self.isEmpty(): 
            return None 
        else: 
            data = self.head.d
            self.head = self.head.next
            return data
         
class BSTree:
    def breadthFirst(self, p): 
        queue = MyQueue()
        queue.EnQueue(p)
        while not queue.isEmpty(): 
            q = queue.DeQueue()
            if q.left != None:
                queue.EnQueue(q.left)
            if q.right != None: 
                queue.EnQueue(q.right)
            self.visit(q)
    def breadthVisit(self): 
        self.breadthFirst(self.root)
    def __init__(self): 
        self.root = None 
    def isEmpty(self): 
        return self.root == None 
    def clear(self): 
        self.root = None 
    def insert(self, data): 
        node = Node(data)
        if self.isEmpty(): 
            self.root = node 
            return 
        cur = self.root
        father = None
        while cur: 
            if cur.data == data: 
                print(f"key {data} is exist")
                return 
            else: 
                father = cur 
                if cur.data < data: 
                    cur = cur.right 
                else: 
                    cur = cur.left
        if father.data < data: 
            father.right = node 
        else: 
            father.left = node 
    
    def visit(self, p): 
        if p:             
            print(f"{p.data} -> ", end = " ")

    def preOder(self, p): 
        if p: 
            self.visit(p)
            self.preOder(p.left)
            self.preOder(p.right)
        else: 
            return 
    def preVisit(self): 
        self.preOder(self.root)

    def postOder(self, p): 
        if p: 
            self.postOder(p.left)
            self.postOder(p.right)
            self.visit(p)
        else: 
            return
    def postVisit(self): 
        self.postOder(self.root)
    
    def inOrder(self, p): 
        if p: 
            self.inOrder(p.left)
            self.visit(p)
            self.inOrder(p.right)
        else: 
            return 
    def inVisit(self): 
        self.inOrder(self.root)

    def deleteByCopyingLeft(self, p):
        if p == None or p.left == None: 
            return
        if p.left.right == None: 
            p.data = p.left.data
            p.left = p.left.left
            return
        cur = p.left.right
        father = p.left 
        while cur.right: 
            father = cur 
            cur = cur.right 
        p.data = cur.data
        father.right = cur.left
    def findNode(self, data): 
        if self.root.data == data: 
            return self.root 
        cur = self.root
        while cur: 
            if cur.data == data: 
                return cur 
            if cur.data < data: 
                cur = cur.right 
            else: 
                cur = cur.left 
        return None 
    #Bai tap: di tim cha cua node co gia tri bang data
    def findFather(self, data): 
        if self.root.data == data: 
            return None 
        fa = None 
        cur = self.root 
        while cur: 
            if cur.data == data: 
                return fa
            fa = cur
            if cur.data < data: 
                cur = cur.right
            else: 
                cur = cur.left
        return None 
        
    #end
    def deleteByMergingLeft(self, data): 
        p = self.findNode(data)
        if not p or not p.left: 
            return 
        cur = p.left
        while cur.right: 
            cur = cur.right 
        father = self.findFather(data)
        cur.right = p.right 
        if father == None: 
            self.root = p.left
        elif father.data < p.data: 
            father.right = p.left 
        else: 
            father.left = p.left 
    
    def deleteByMergingLeft02(self, data): 
        p = self.findNode(data)
        if not p or not p.left: 
            return 
        cur = p.left 
        while cur.right: 
            cur = cur.right 
        cur.right = p.right 
        p.data = p.left.data
        p.right = p.left.right 
        p.left = p.left.left 
    # Kiểm tra chiều cao của cây 
    def getHeight(self, p):
        if  p == None: 
            return 
        if p.left == None and p.right == None: 
            return 0
        return max(self.getheight(p.left)), self.getHeight(p.right) + 1 
    
    # QUay cây 
    def rightRotate(self, p): 
        if not p or not p.left: 
            return 
        c = p.left 
        p.left = c.right 
        c.right = p 
        return c 
    
    def rightRotation(self, data):
        f = self.findFather(data)
        p = None 
        if f == None: 
            if (self.root.data != data): 
                return 
            else: 
                p = self.root 
        else: 
            if (f.data > data): 
                p = f.left 
            else: 
                p = f.right
        newNode = self.rightRotate(p)
        if f == None: 
            self.root = newNode
        else: 
            if (f.left.data < data): 
                f.right = newNode
            else: 
                f.left = newNode

t = BSTree()
t.insert(8)
t.insert(4)
t.insert(12)
t.insert(2)
t.insert(6)
t.insert(10)
t.insert(14)
t.insert(1)
t.insert(7)
t.insert(5)
t.insert(3)
t.insert(15)
t.insert(13)
t.insert(11)
t.insert(9)
t.inVisit()
print()
t.preVisit()
print()
t.postVisit()
print()
t.breadthVisit()
print("delete node 8")
# t.deleteByCopyingLeft(t.root)
# t.deleteByCopyingLeft(t.root.left)
# t.deleteByMergingLeft02(4)
t.rightRotation(10)

t.breadthVisit()
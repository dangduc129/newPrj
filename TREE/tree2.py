
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
#

class Node:
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.pre = None 

class DBLL:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0  
    
    def isEmpty(self): 
        return self.size == 0 
    
    def addFirst(self, data): 
        node = Node(data)
        if self.isEmpty():
            self.head = self.tail 
        else: 
            node.next = self.head
            self.head.pre = node 
            self.head = node 
        self.size += 1 
            
    def display(self): 
        if self.isEmpty(): 
            return 
        cu = self.head 
        while cu: 
            print(f{cu.data}", end = "")
            cu.next

A = DBLL()
A.addFirst(5)
A.addFirst(6)
A.addFirst(7)"
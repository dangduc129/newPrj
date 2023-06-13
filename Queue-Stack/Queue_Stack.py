# # Thiet ke chuong trinh List : Queue & Stack 
# # 1 Queue (FIFO): 
# # Enqueue <--> addLast 
# # Dequeue <--> delLast 
# # ----------------------
# # 1 Stack(LIFO): 
# # Push <--> addFirst 
# # Pop <--> delFirst 
# # Top 

# import re
# class Empty(Exception):
#     pass
# class Stack:
#     def __init__(self): 
#         self.a = []
#         self._data = []
    
#     def __len__(self):
#         return len(self._data)
    
#     def is_empty(self):
#         return len(self._data) == 0
    
#     def push(self, e):
#         self._data.append(e)
    
#     def top(self):
#         if self.is_empty():
#             raise Empty('Stack is empty')
#         return self._data[-1]
    
#     def pop(self):
#         if self.is_empty():
#             raise Empty('Stack is empty')
#         return self._data.pop()
    
#     def readFile(self): 
#         with open('dataa.txt', 'r') as file:
#             for line in file:
#                 print(line.strip())

#     def reverse_file(self):
#         S = Stack()
#         with open('dataa.txt', 'r') as file:
#             for line in file: 
#                 S.push(line.rstrip("\n"))
#         with open("dataa.txt", 'w') as file:
#             while not S.is_empty(): 
#                 file.write(S.pop()+ "\n")
#             print()
#     def write_file(self): 
#         with open('dataa.txt', 'w') as file: 
#             file.write('abc')
# def main(): 
#     S = Stack()
#     # S.write_file()
#     S.readFile()
#     S.reverse_file()
# main()
    
# class Stack: 
#     def __init__(self): 
#         self.data = data

#     def isEmpty(self): 
#         return len(self.data) == 0

#     def push(self,e):
#         self.data.append(e)

#     def pop(self): 
#         while not self.isEmpty(): 
#             return self.data.pop() 
#     def readFile(self, fileName):
#         S = Stack()
#         with open(fileName,'r') as file:
#             for line in file: 
#                 S.push(line.rstrip('\n'))
#         with open(fileName,'w') as file:
#             while not self.isEmpty():
#                 file.write(S.pop() + '\n')
#             print()
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def display(self): 
#         print(f"{self.data}", end ="\n")
# class Stack:
#     def __init__(self):
#         self.top = None
#     def is_empty(self):
#             return self.top is None
#     def peek(self):
#             return self.top.data
     
#     def push(self, data):
#         node = Node(data)
#         node.next = self.top
#         self.top = node
#     def pop(self):
#             data = self.top.data
#             self.top = self.top.next
#             return data
#     def reverse_data_from_file(self,fileName): 
#         with open(fileName, 'w') as file: 
#             total = input("Please write: ")
#             for i in range(int(total)): 
#                 self.push = str(input("so: "))
#                 file.write(self.push + '\n')
#         with open(fileName,'r') as file: 
#             for line in file:
#                 Stack.pop()
            
#     def display(self): 
#         cur = self.top
#         while cur:
#             cur.display()
#             cur = cur.next
        
# def main(): 
#     S = Stack()
#     # S.push(5)
#     # S.push(6)
#     # S.push(7)
#     # S.push(8)
#     S.reverse_data_from_file('dataa.txt')
#     S.display()
# main()
# --------------------------------
# class Empty(Exception): 
#     pass 
# class Stack: 
#     def __init__(self): 
#         self.data = []
        
#     def len(self): 
#         return len(self.data) 
    
#     def isEmpty(self): 
#         return len(self.data) == 0 
    
#     def push(self,a): 
#         list = self.data.append(a)
#         return list 
#     def top(self): 
#         if self.isEmpty(): 
#             raise Empty('Stack is empty')
#         return self.data[-1]

#     def pop (self): 
#         if self.isEmpty(): 
#             raise Empty('Stack is empty')
#         return self.data.pop()
    
#     def display(self): 
#         print(f"{self.data}", end = " ")
# S = Stack()
# S.push(5)        
# S.push(6)        
# S.push(7)    
# S.top()    
# S.display()
#END CLASS 

import numpy.random as rd 
st = rd.randint(100,size =(20))
st = list(st)
print(st)

# max = st[0]
# for i in range(1, len(st)):
#     if st[i] > max:
#         max = st[i]

# print("Max: ",max)
m = st.pop()
while (st!=[]): 
    b = st.pop()
    if b>m: 
        m = b 
print(m)

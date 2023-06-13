import re 
from Queue import *
class Euler: 
    def __init__(self, fileName): 
        self.fileName = fileName 
        self.a = []

    def readFile(self): 
        f1 = open(self.fileName,"r")
        line = f1.readline()
        while True: 
            line = f1.readline()
            if not line: 
                break 
            row = re.sub("\s+"," ",line.strip()).split(" ")
            b = []
            for i in range(len(row)): 
                b.append(int(row[i]))
            self.a.append(b)
        f1.close()
        for i in range(len(self.a)): 
            for j in range(i+1, len(self.a[i])): 
                self.a[j][i] = self.a[i][j]
        
    def display(self):
        for i in range(len(self.a)): 
            for j in range(len(self.a[i])): 
                print(f"{self.a[i][j]}", end = " ")
            print()
        print()
    
    def visit(self, p): 
        print(f"{chr(p+65)}", end = " -> ")

    def degree(self, x): 
        t = 0 
        for i in range(len(self.a)): 
            t += self.a[i][x]
        return t 

    def connectivity(self): 
        #Kiem tra xem do thi co lien thong hay ko bang cach duyet tat cac dinh, neu nhu co dinh chua visit thi tra ve False, con ko thi tra ve True 
        pass
    def checkEuler(self): 
        #DO THI LIEN THONG- tat ca cac bac cua cac dinh phai la chan --> Co chu trinh Euler //chi co 2 dinh bac le thi co duong di Euler 
        pass 

    def Euler(self, start): 
        p = ord(start)-65
        s = Stack()
        s.push(p)
        e = []
        while not s.isEmpty(): 
            q = s.top()
            if self.degree(q) == 0:
                s.pop()
                e.append(q)
            else: 
                for i in range(len(self.a)): 
                    if self.a[i][q] != 0:
                        s.push(i)
                        self.a[i][q] -=1 
                        self.a[q][i] -=1
                        break 
        for x in e: 
            self.visit(x)

e = Euler("matrix1.txt")
e.readFile()
e.display()
e.Euler('A')
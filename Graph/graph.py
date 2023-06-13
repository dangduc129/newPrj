import re 
from Queue import *

class Graph: 
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
            for j in range(len(self.a[i])): 
                self.a[j][i] = self.a[i][j]
        
    def display(self):
        for i in range(len(self.a)): 
            for j in range(len(self.a[i])): 
                print(f"{self.a[i][j]}", end = " ")
            print()
        print()

    def visit(self, i): 
        print(f"{chr(i+65)}", end = " -> ")
    def breadth_first(self, x): 
        visited = [True]*len(self.a)
        y = ord(x)-65
        queue = Queue()
        queue.Enqueue(y)
        visited[y] = False
        while(not queue.isEmpty()): 
            q = queue.Dequeue()
            self.visit(q)
            for i in range(len(self.a)):
                if visited[i] and self.a[i][q] ==1: 
                    visited[i] = False
                    queue.Enqueue(i)
    #end def
    def deepth_visit(self, start): 
        p = ord(start) - 65
        b = [True]*len(self.a)
        b[p] = False
        self.deepth(p, b)
    #end def 
    def deepth(self, start, b): 
        self.visit(start)
        for i in range(len(self.a)): 
            if b[i] and self.a[i][start] == 1:
                b[i] = False
                self.deepth(i,b)

g = Graph("matrix.txt")
g.readFile()
g.display()
# g.breadth_first('A')
g.deepth_visit('A')


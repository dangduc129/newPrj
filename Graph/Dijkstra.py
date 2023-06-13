import re
class Dijkstra: 
    def __init__(self, fileName): 
        self.fileName = fileName 
        self.a = []

    def readFile(self): 
        with open(self.fileName, 'r') as file: 
            lines = file.readlines()
            # lines = [line.replace('\n','') for line in lines]
            # lines = [line.replace('\t','') for line in lines]
            lines = [line.split() for line in lines]
            lines = [[int(point) for point in line ] for line in lines]
            self.a = lines 
        for i in range(len(self.a)): 
            for j in range(len(self.a)): 
                self.a[j][i] = self.a[i][j]
    def display(self): 
        for i in range(len(self.a)): 
            for x in self.a[i]: 
                print(x, end = " ")
            print()

    #end def 
    path = []
    dist = []
    def toInt(self,x): 
        return ord(x) - 65 
    def shortestPath(self, fro, to): 
        f = self.toInt(fro)
        t = self.toInt(to)
        inf = 99 
        n = len(self.a)
        selected = [True]*n
        selected[f] = False
        for i in range(n):
            self.path.append(f)
            self.dist.append(self.a[f][i])
        while True:
            k=-1 
            mmin = inf 
            for i in range(n):
                if selected[i] and self.dist[i] < mmin:
                    mmin = self.dist[i]
                    k = i
            if k == -1: 
                print("No solution!!!")
                return 
            if k == t: 
                break
            selected[k] = False 
            for i in range(n): 
                if (selected[i]): 
                    if (self.dist[i] > self.dist[k] + self.a[i][k]):
                        self.dist[i] = self.dist[k] + self.a[i][k]
                        self.path[i] = k
        self.showPath(fro,to)
    def showPath(self, fro, to): 
        stack = []
        i = self.toInt(to)
        stack.append(i)
        while True: 
            i = self.path[i]
            stack.append(i)
            if i == self.toInt(fro): 
                break 
        while stack: 
            i = stack.pop()
            print(f"{chr(i+65)}({self.dist[i]})", end ="")
            if i != self.toInt(to): 
                print("->", end ="")

d = Dijkstra("graph.txt")
d.readFile()
d.display()
d.shortestPath('A','F')

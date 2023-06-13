def fact(n): 
    if n == 0: 
        return 1 
    else: 
        return n*fact(n-1)

def multi(a, b): 
    if b == 0: 
        return 0 
    else: 
        return multi(a, b-1) + a 

def pow(a,b): 
    if b == 0: 
        return 1 
    else: 
        return pow(a,b-1)*a

def move(n, a, b, c): 
    if n == 1: 
        print(f"Move {a} -> {b}")
    else: 
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, c, b, a )
import numpy
class knight: 
    def __init__(self, size): 
        self.size = size 
        b = []
        for i in range(0, size): 
            x = []
            for j in range(0,size):
                x.append(0)
            b.append(x)
        self.a = b 
    
    def move(self, x, y): 
        self.a[x][y] = 1 
        count = 1 
        self.dichuyen(count, x ,y)
    def check(self, x): 
        return x>=0 and x < self.size
    def dichuyen(self, count, x, y): 
        xx = [-2,-1,1,2,2,1,-1,-2]
        yy = [1,2,2,1,-1,-2,-2,-1]
        if count == self.size*self.size : 
            self.display()
        else: 
            for i in range(8): 
                x1 = x + xx[i]
                y1 = y + yy[i]
                if (self.check(x1) and self.check(y1) and self.a[x1][y1] == 0):
                    self.a[x1][y1] = count+1 
                    self.dichuyen(count+1, x1, y1)
                    self.a[x1][y1] = 0


    def display(self): 
        for i in range(self.size): 
            for j in range(self.size): 
                print(self.a[i][j], end =" ")
            print("")
        print("Them cach")
k = knight(6)
k.move(1,2)

# n = int(input("Input n: "))
# print(f"fact(${n}) = {fact(n)}")
# print(multi(3,4))
# move(4, 'A', 'B', 'C')


import random
class Heap: 
    def __init__(self, a): 
        self.a = a 

    def check(self): 
        for i in range(len(self.a)):
            if (self.a[i] > self.a[(i-1)//2]):
                return False
        return True
    
    def checkSort(self): 
        for i in range(len(self.a) - 1): 
            if self.a[i] > self.a[i+1]: 
                return False
        return True
    def toHeap(self): 
        n = len(self.a)
        for i in range(1, n): 
            temp = self.a[i]
            c = i 
            f = (i-1)//2 
            while (self.a[f] < temp and f>=0):
                self.a[c] = self.a[f]
                c = f 
                f = (c-1)//2
            self.a[c] = temp
    def headSort(self): 
        n = len(self.a)
        for i in range(n-1, 0, -1): 
            temp = self.a[i]
            self.a[i] = self.a[0]
            c = 1 
            while c < i: 
                if c + 1 < i and self.a[c+1] > self.a[c]: 
                    c = c+1 
                if self.a[c] >temp: 
                    self.a[(c-1)//2] = self.a[c]
                    c = 2*c + 1 
                else: 
                    break 
            self.a[(c-1)//2] = temp
    def display(self): 
        for i in a : 
            print(f"{i}", end =" ")
        print()

a = []
for i in range(10): 
    a.append(random.randint(0,100))
h = Heap(a)
h.display()
h.toHeap()
h.display()
h.headSort()
h.display()
print(f"check = {h.checkSort()}")
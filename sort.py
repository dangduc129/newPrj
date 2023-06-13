#MERGR SORT: 

import random
class Sort: 
    def __init__(self, n, a): 
        self.n = n #kichs thuoc cua mang 
        self.a = a #mang nguyen 
    #end def 
    def display(self):
        for i in self.a:
            print(f"{i}", end = " ")
        print()
    #end def 
    def mergeSort(self): 
        self.mSort(0, self.n)
    def check(self): 
        for i in range(0, n-1): 
            if self.a[i]>self.a[i+1]: 
                return False
        return True
    def mSort(self, b, e): #Tinhs den truoc e 
        if e <= b+1:
            return
        elif e == b+2:
            if self.a[b]> self.a[b+1]:
                t = self.a[b]
                self.a[b] = self.a[b+1]
                self.a[b+1] = t 
        else:
            m = (b+e)//2
            self.mSort(b, m)
            self.mSort(m, e)
            self.join(b, e, m)
    def join(self, b, e, m): 
        c = []
        i = b 
        j = m 
        while i < m and j < e: 
            if self.a[i] < self.a[j]: 
                c.append(self.a[i])
                i +=1 
            else: 
                c.append(self.a[j])
                j +=1   
        if i==m: 
            while j < e: 
                c.append(self.a[j])
                j +=1 
        else: 
            while i < m: 
                c.append(self.a[i])
                i +=1
        for i in range(b, e): 
            self.a[i] = c[i-b]
#QUICK SORT: 
    def QuickSort(self): 
        self.QSort(0, self.n-1)
    def QSort(self, b, e): #cos tinh phan tu cuoi 
        if b >= e: 
            return 
        elif b+1== e: 
            if self.a[b]>self.a[e]: 
                t = self.a[b]
                self.a[b] = self.a[e]
                self.a[e] = t 
        else: 
            pivot = self.getPivot(b, e)
            self.QSort(b, pivot-1)
            self.QSort(pivot+1,e)
    def getPivot(self, b, e): 
        pivot = self.a[e]
        up = b 
        down =e 
        while up < down : 
            while up < down and self.a[up]<pivot: 
                up+=1 
            while down >= up and self.a[down] >= pivot: 
                down -=1 
            if up < down: 
                t = self.a[down]
                self.a[down] = self.a[up]
                self.a[up] = t 
        
        self.a[e] = self.a[up]
        self.a[up] = pivot 
        return up
n = int(input("Input size of array: "))
a = [random.randint(0,999) for i in range(n)]
print(a)
sort = Sort(n, a)
# sort.mergeSort()
sort.QuickSort()
sort.display()
print(sort.check())




     




import re 

class sudoku: 
    def __init__(self, fileName): 
        f1 = open(fileName, 'r')
        self.a = []
        while True: 
            line = f1.readline()
            if not line: 
                break
            listValue = re.sub("\s+"," ",line.strip()).split(" ")
            row = []
            for i in range(len(listValue)): 
                row.append(int(listValue[i]))
            self.a.append(row)
    
    def display(self): 
        for i in range(9): 
            for j in range(9): 
                print(self.a[i][j], end = " ")
            print()
        print()

    def fillUp(self, x, y): 
        if y == 9: 
            if x == 8: 
                self.display()
            else: 
                self.fillUp(x+1, 0)
        else: 
            if self.a[x][y]!= 0: 
                self.fillUp(x, y + 1)
            else: 
                b = [True]*10 
                for i in range(9): 
                    b[self.a[x][i]] = False 
                    b[self.a[i][y]] = False 
                for i in range(x//3*3, x//3*3 + 3):
                    for j in range(y//3*3, y//3*3 + 3):
                        b[self.a[i][j]] = False
                for i in range(1,10): 
                    if b[i] == True: 
                        self.a[x][y] = i 
                        self.fillUp(x, y + 1)
                        self.a[x][y] = 0



s = sudoku("input.txt")
s.fillUp(0,0)
s.display()
#Bài toán vét cạn, bài toán quay lui cần đệ quy 
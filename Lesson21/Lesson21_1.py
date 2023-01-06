class Matrix:

    def __init__(self,mtr=None,det=None,rank=None,x=0,y=0):
        self.det = det
        self.rank=rank
        if mtr:
            self.mtr = mtr
            self.x=len(mtr[0])
            self.y=len(mtr)
            self.det=Matrix.deter(self)
        else:
            self.mtr = None
            self.x = 1
            self.y = 1

    def __str__(self):
        if self.mtr:
            cmpl=False
            max=1
            l=0
            r=0
            non=0
            for i in range(self.y):
                for j in range(self.x):
                    s = str(self.mtr[i][j])
                    if self.mtr[i][j]==None:
                        non+=1
                    if isinstance(self.mtr[i][j],complex):
                        cmpl=True
                    parts=s.partition(".")
                    if len(parts[0])>l:
                        l=len(parts[0])
                    if len(parts[2])>r:
                        r=len(parts[2])
                    if max<len(str(self.mtr[i][j])):
                        max=len(str(self.mtr[i][j]))
            if non>0 and non < self.x*self.y:
                print("У матриці є частково незаповнені значення.")
                return ""
            elif non == self.x*self.y:
                print(f'Matrix {self.y}x{self.x}   Determinant={self.det}')
                for i in range(self.y):
                    print("|", end="")
                    for j in range(self.x - 1):
                        print(self.mtr[i][j], " ", end="")
                    print(self.mtr[i][-1], "|")
                return ""
            if cmpl:
                for i in range(self.y):
                    for j in range(self.x):
                        self.mtr[i][j]=complex(self.mtr[i][j])
                        if max < len(str(self.mtr[i][j])):
                            max = len(str(self.mtr[i][j]))
                st="{:{align}{width}}"
            else:
                st="{:{align}{width}.{precision}f}"
            print(f'Matrix {self.y}x{self.x}   Determinant={self.det}')
            for i in range(self.y):
                print("|",end="")
                for j in range(self.x-1):
                    if cmpl:
                        print(st.format(self.mtr[i][j], align='>', width=max), " ", end="")
                    else:
                        print(st.format(self.mtr[i][j],align='>', width=l+r+1, precision=r)," ",end="")
                if cmpl:
                    print(st.format(self.mtr[i][-1], align='>', width=max), "|")
                else:
                    print(st.format(self.mtr[i][-1],align='>', width=l+r+1, precision=r),"|")
        else:
            print(f"|{self.mtr}|")
        return ""

    def transpon(self):
        b=list()
        c=list()
        if self.mtr:
            for i in range(self.x):
                c=[]
                for j in range(self.y):
                    c.append(None)
                b.append(c)
            for i in range(self.y):
                for j in range(self.x):
                    b[j][i]=self.mtr[i][j]
            return Matrix(b)
        else:
            return Matrix(None)


    def minor(a,k,l):
        c=list()
        d=list()
        for i in range(a.x):
            c = []
            for j in range(a.x):
                if j!=l-1 :
                    c.append(a.mtr[i][j])
            if i!=k-1 :
                d.append(c)
        p=Matrix(d)
        # print(p)
        return p

    def dopolnenie(list_matrica):
        new = list()
        for i in range(list_matrica[1].x):
            new.append([None, None])
        for i in range(list_matrica[1].x):
            new[i][0] = list_matrica[0] * list_matrica[1].mtr[0][i] * (-1) ** i
            new[i][1] = Matrix.minor(list_matrica[1], 1, i + 1)
        return new


    def deter(m):
        sum=0
        if  m.x==m.y :
            if  m.x == 1:
                return m.mtr[0][0]
            elif m.x==2:
                return m.mtr[0][0]*m.mtr[1][1]-m.mtr[1][0]*m.mtr[0][1]
            elif m.x>2:
                ls=[[1,m]]
                for j in range(m.x-1):
                    n=len(ls)
                    ls_new = []
                    ls_new1=[]
                    for i in ls:
                        ls_new=Matrix.dopolnenie(i)
                        for k in ls_new:
                            ls_new1.append(k)
                    ls.clear()
                    ls=ls_new1
                for i in range(len(ls)):
                    sum=sum+ls[i][0]*ls[i][1].mtr[0][0]
                return sum
        else:
            return None




    def add(self,b):
        if  isinstance(b,Matrix):
            if self.x==b.x and self.y==b.y:
                for i in range(self.y):
                    for j in range(self.x):
                        self.mtr[i][j] += b.mtr[i][j]
                return self
            else:
                print("Матриці мають різну розмірність ця операція не допустима")
                return None
        else:
            print("Не відповідність типів даних! Аргумент функції Matrix.add повинен бути об'єктом типу Matrix.")
            return None

    def add_num(self,b):
        for i in range(self.y):
            for j in range(self.x):
                self.mtr[i][j] += b
        return self

    def sub_num(self,b):
        for i in range(self.y):
            for j in range(self.x):
                self.mtr[i][j] -= b
        return self

    def mult_num(self,b):
        for i in range(self.y):
            for j in range(self.x):
                self.mtr[i][j] *= b
        return self

    def div_num(self,b):
        for i in range(self.y):
            for j in range(self.x):
                self.mtr[i][j] /= b
        return self

    def __add__ (self,b):
            d = list()
            c = list()
            if isinstance(self,Matrix) and isinstance(b,(Matrix, int, float, complex)):
                if (isinstance(self,Matrix) and isinstance(b,Matrix)) and (self.x!=b.x or self.y!=b.y):
                    return "Матриці мають різну розмірність ця операція не допустима"
                else:
                    for i in range(self.y):
                        c = []
                        for j in range(self.x):
                            c.append(None)
                        d.append(c)
                    for i in range(self.y):
                        for j in range(self.x):
                            if isinstance(b,Matrix):
                                d[i][j] = self.mtr[i][j] + b.mtr[i][j]
                            else:
                                d[i][j] = self.mtr[i][j] + b
                    return Matrix(d)
            else:
                return "Не відповідність типів даних! Аргументи функції '+' повинні бути об'єктами типу Matrix, Int, Float або Complex"

    def __radd__(self, b):
        d = list()
        c = list()
        if isinstance(self, Matrix) and isinstance(b, (int, float, complex)):
            for i in range(self.y):
                c = []
                for j in range(self.x):
                    c.append(None)
                d.append(c)
            for i in range(self.y):
                for j in range(self.x):
                    d[i][j] = self.mtr[i][j] + b
            return Matrix(d)
        else:
            return "Не відповідність типів даних! Аргументи функції '+' повинні бути об'єктами типу Matrix, Int, Float або Complex"

    def __sub__ (self,b):
            d = list()
            c = list()
            if isinstance(self,Matrix) and isinstance(b,(Matrix, int, float, complex)):
                if (isinstance(self,Matrix) and isinstance(b,Matrix)) and (self.x!=b.x or self.y!=b.y):
                    return "Матриці мають різну розмірність ця операція не допустима"
                else:
                    for i in range(self.y):
                        c = []
                        for j in range(self.x):
                            c.append(None)
                        d.append(c)
                    for i in range(self.y):
                        for j in range(self.x):
                            if isinstance(b,Matrix):
                                d[i][j] = self.mtr[i][j] - b.mtr[i][j]
                            else:
                                d[i][j] = self.mtr[i][j] - b
                    return Matrix(d)
            else:
                return "Не відповідність типів даних! Аргументи функції '+' повинні бути об'єктами типу Matrix, Int, Float або Complex"

    def __mul__ (self,b):
            d = list()
            c = list()
            if isinstance(self,Matrix) and isinstance(b,(Matrix, int, float, complex)):
                if (isinstance(self,Matrix) and isinstance(b,Matrix)) and (self.x!=b.x or self.y!=b.y):
                    return "Матриці мають різну розмірність ця операція не допустима"
                else:
                    for i in range(self.y):
                        c = []
                        for j in range(self.x):
                            c.append(None)
                        d.append(c)
                    for i in range(self.y):
                        for j in range(self.x):
                            if isinstance(b,Matrix):
                                d[i][j] = self.mtr[i][j] + b.mtr[i][j]
                            else:
                                d[i][j] = self.mtr[i][j] + b
                    return Matrix(d)
            else:
                return "Не відповідність типів даних! Аргументи функції '+' повинні бути об'єктами типу Matrix, Int, Float або Complex"

    def __rmul__(self, b):
        d = list()
        c = list()
        if isinstance(self, Matrix) and isinstance(b, (int, float, complex)):
            for i in range(self.y):
                c = []
                for j in range(self.x):
                    c.append(None)
                d.append(c)
            for i in range(self.y):
                for j in range(self.x):
                    d[i][j] = self.mtr[i][j] * b
            return Matrix(d)
        else:
            return "Не відповідність типів даних! Аргументи функції '+' повинні бути об'єктами типу Matrix, Int, Float або Complex"

    def __truediv__(self, b):
        d = list()
        c = list()
        if isinstance(self, Matrix) and isinstance(b, (int, float, complex)):
            for i in range(self.y):
                c = []
                for j in range(self.x):
                    c.append(None)
                d.append(c)
            for i in range(self.y):
                for j in range(self.x):
                    d[i][j] = self.mtr[i][j] / b
            return Matrix(d)
        else:
            return "Не відповідність типів даних! Аргументи функції '+' повинні бути об'єктами типу Matrix, Int, Float або Complex"

    def one_mtr(n):
        d = list()
        c = list()
        for i in range(n):
            c = []
            for j in range(n):
                if i==j :
                    c.append(1)
                else:
                    c.append(0)
            d.append(c)
        return Matrix(d)



lst=[[1,2,5],
     [6,-4,7],
     [8,5,9]]

lst1=[[1,2,3,4],[6,4,7,3],[8,5,9,2],[3,4,2,6]]
lst3=[[1,2.5,3,4,5],[6,4,7,3,5],[8,5.3,9,2,5],[3,4,2,6,5],[5,4,3,2,1]]

lst2=[[6,8],
      [4,7]]

a=Matrix(lst3)
print(a.det)
b=Matrix(lst)

print(a)
print(Matrix.deter(a))

# d=Matrix.minor(a,2,2)
# print(d)
# d2=Matrix.one_mtr(5)
# d3=a+b-5
#
# print(d1)
# print(d2)
# print(d3)




# print(a.mult_num(5))
# print(a.div_num(3))
# d=Matrix.add(a,a)
# print(d)
# print(a.mtr,a.x,a.y)



#  Клас Matrix створено для роботи із матрицями різних розмірностей
# Створення екземпляру класу можливо або пустим або з одночасною передачею в якості аргумента вкладеного списку.
# В класі визначені усі математичні операції для роботи з екземплярами класу використовуючі звичайні операнди +-*/
# Матриці створені в класі можуть працювати із даними типу Int,Float,Complex
# В класі визначена процедура візуалізації екземпляру класу для виводу на екран.

class Matrix:
    def __init__(self,mtr=None,det=None,x=0,y=0):
        if mtr:
            self.mtr = mtr              # Список у якому зберігаються елементи матриці із можливістю доступу за форматом mtr[i][j]
            self.x=len(mtr[0])          # Кількість рядків
            self.y=len(mtr)             # Кількість строк
            self.det=Matrix.deter(self) # Детермінант матриці
        else:
            self.mtr = None
            self.x = 1
            self.y = 1

    #  Визначення виду матриці яка виводиться на печать викликається командою print(A)
    # Одночасно із виведенням на печать основної матриці друкується довідкова інформація про матрицу
    # розмірність, детермінант та ранг
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
            print(f'Matrix {self.y}x{self.x}   Determinant={self.det}  Rank={self.rank()}')
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

    # Функція дозволяє створювати копію екземпляру класу без зміни оригіналу
    def copy(self):
        b=[]
        for i in range(self.y):
            c = []
            for j in range(self.x):
                c.append(None)
            b.append(c)
        for i in range(self.y):
            for j in range(self.x):
                b[i][j]=self.mtr[i][j]
        return Matrix(b)

    # Функція дозволяє проводити транспонування переданої матриці із створенням нової транспонованої копії
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

    # Функія визначає мінор будь-якого елементу матриці.
    # В якості аргументів функція приймає матрицю а та [k],[l] - строка, стовбчик елемента матриці до якого будується мінор
    def minor(a,k,l):
        c=list()
        d=list()
        for i in range(a.y):
            c = []
            for j in range(a.x):
                if j!=l-1 :
                    c.append(a.mtr[i][j])
            if i!=k-1 :
                d.append(c)
        p=Matrix(d)
        return p


    # Службова функція яка будує доповнення до елементу матриці при розрахунку детермінанту згідно правил розкладення
    # детермінанта за елементами строки
    def dopolnenie(list_matrica):
        new = list()
        for i in range(list_matrica[1].x):
            new.append([None, None])
        for i in range(list_matrica[1].x):
            new[i][0] = list_matrica[0] * list_matrica[1].mtr[0][i] * (-1) ** i
            new[i][1] = Matrix.minor(list_matrica[1], 1, i + 1)
        return new

    # Функція вираховує детермінант матриці
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

    # Функція дозволяє складати дві матриці однакових розмірів зі зміною екземпляру класу
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

    # Функція дозволяє додавати числове значення до всіх елементів матриці зі зміною оригіналу
    def add_num(self,b):
        for i in range(self.y):
            for j in range(self.x):
                self.mtr[i][j] += b
        return self

    # Функція дозволяє віднімати числове значення від всіх елементів матриці зі зміною оригіналу
    def sub_num(self,b):
        for i in range(self.y):
            for j in range(self.x):
                self.mtr[i][j] -= b
        return self

    # Функція дозволяє множити числове значення на всі елементи матриці зі зміною оригіналу
    def mult_num(self,b):
        for i in range(self.y):
            for j in range(self.x):
                self.mtr[i][j] *= b
        return self

    # Функція дозволяє поділити всі елементи матриці на  числове значення зі зміною оригіналу
    def div_num(self,b):
        for i in range(self.y):
            for j in range(self.x):
                self.mtr[i][j] /= b
        return self

    # Функція проводить перевизначення операції + для об'єктів класу в залежності від того які типи даних складаються
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

    # Функція проводить перевизначення операції + для об'єктів класу (в іншу сторону) в залежності від того які типи даних складаються
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

    # Функція проводить перевизначення операції - для об'єктів класу в залежності від того які типи даних віднімаються
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

    # Функція проводить перевизначення операції * для об'єктів класу в залежності від того які типи даних перемножуються
    # Коректно працює при перемноженні матриць, у відповідності, до математичних правил
    def __mul__ (self,b):
            d = list()
            c = list()
            if isinstance(self,Matrix) and isinstance(b,(Matrix, int, float, complex)):
                if (isinstance(self,Matrix) and isinstance(b,Matrix)) and (self.y!=b.x):
                    return "Матриці мають різну розмірність ця операція не допустима"
                elif (isinstance(self,Matrix) and isinstance(b,Matrix)) and (self.y==b.x):
                    for i in range(self.y):
                        c = []
                        for j in range(b.x):
                            c.append(0)
                        d.append(c)
                    for i in range(self.y):
                        for j in range(b.x):
                             for k in range(self.x):
                                 d[i][j]=d[i][j]+self.mtr[i][k]*b.mtr[k][j]
                    return Matrix(d)
                else:
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

    # Функція проводить перевизначення операції * (в іншу сторону) для об'єктів класу в залежності від того які типи даних перемножуються
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

    # Функція проводить перевизначення операції /  для об'єктів класу в залежності від того які типи даних діляться
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

    # Функція генерує одиничну матрицю розмірністю n*n
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

    # Функція проводить ступінчате перетворення матриці за методом Гаусса та будує верхню трикутну матрицю
    def triangl_transform(self):
        if self.x!=self.y:
            print("Функція може проводити перетворення тільки квадратних матриць. Перевірте параметри матриці!")
            return None
        a = self.copy()
        if a.mtr[0][0]==0 and a.x>1:
            i=1
            n=0
            while True:
                if a.mtr[i][0]!=0:
                    n=i
                    break
                i+=1
            if n==0:
                print("Перший стовбчик матриці має всі нульові значення. Перевірте параметри матриці!")
                return None
            for i in range(a.x):
                a.mtr[0][i],a.mtr[n][i]=a.mtr[n][i],a.mtr[0][i]
        n = a.mtr[0][0]
        for i in range(a.x):
            a.mtr[0][i]=a.mtr[0][i]/n
        for j in range(a.x-1):
            ls = []
            for k in range(j+1,a.x):
                for i in range(a.x):
                    a.mtr[k][i]=a.mtr[k][i]+(-1)*a.mtr[k][i]*a.mtr[j][i]
            n=a.mtr[j+1][j+1]
            for i in range(a.x):
                a.mtr[j+1][i] = a.mtr[j+1][i] /n
        return a

    # Функція вираховує ранг матриці
    def rank(m):
        if m.x!=m.y:
            print("Функція може розраховувати ранг тільки для квадратних матриць")
            return None
        if m.x==0:
            return 0
        elif m.x==1 and m.mtr[0][0]==0:
            return 0
        elif m.x==1 and m.mtr[0][0]!=0:
            return 1
        elif m.x>=2:
            a=m.triangl_transform()
            n=0
            k=0
            for i in range(a.x):
                for j in range(i,a.y):
                    if a.mtr[i][j]==0:
                        n+=1
                if n==a.x-i:
                    k+=1
        return a.x-k


lst=[[3,2,3],
     [2,-14,4],
     [8,15,9]]
lst1=[[1,2,3,4],[6,4,7,3],[8,5,9,2],[3,4,2,6]]
lst2=[[3,9], [2,4]]
lst3=[[-5,25,3,4,5],[6,4,-7,3,5],[8,5,9,2,5],[3,4,2,6,5],[5,4,3,2,1]]
lst4=[[14,2,9],
     [1,-7,2],
     [-6,3,8]]
lst5=[[2,3],[4,6]]


print(Matrix(lst1))
a=Matrix(lst4)
b=Matrix(lst)
c=a*b
print(c)
c=a-b
print(c)
c=a+b
print(c)
c=a*5
print(c)
c=a-5
print(c)
c=a/5
print(c)
print(Matrix.one_mtr(3))
a=Matrix(lst)
print(a.sub_num(3))
print(a.mult_num(3))
print(c.add_num(-5))
print(b.div_num(3))
print(a.add(b))
c=Matrix(lst3)
print(c.triangl_transform())



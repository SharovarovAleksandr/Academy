import math

def kvadrat(a) :
    s=a*a
    p=4*a
    d=a*math.sqrt(2)
    return s,p,d

x=float(input("Сторона квадрату: "))
print("Площа     :",kvadrat(x)[0])
print("Периметр  :",kvadrat(x)[1])
print("Діагональ :",kvadrat(x)[2])
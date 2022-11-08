def polindrom(a):
    a=a.replace(" ","")
    b=list(a)
    b.reverse()
    c=list(a)
    if b==c:
        return True
    else:
        return False


a="випив"
b="а роза упала на лапу азора"
c="не випив"
d="кит на морі романтик"
print(polindrom(a))
print(polindrom(b))
print(polindrom(c))
print(polindrom(d))

from binarytree import *

def serch_max(self):
    ls=list(self.values)
    if len(ls)==0:
        print("Такого дерева не існує")
        return None
    elif len(ls)==1:
        return ls[0]
    elif not self.is_bst:
        print("Функція serch_max може шукати найбільший елемент тільки у BTS. Це дерево не відповідає критеріям BTS ")
        return None
    else:
        i=1
        max=ls[0]
        while i<=self.height:
           j=int((2**(i+1))-2)
           try:
               if ls[j]>max:
                   max=ls[j]
           except TypeError:
               return max
           except IndexError:
               return max
           i+=1
    return max

def serch_min(self):
    ls=list(self.values)
    if len(ls)==0:
        print("Такого дерева не існує")
        return None
    elif len(ls)==1:
        return ls[0]
    elif not self.is_bst:
        print("Функція serch_max може шукати найбільший елемент тільки у BTS. Це дерево не відповідає критеріям BTS ")
        return None
    else:
        i=1
        min=ls[0]
        while i<=self.height:
           j=int((2**i)-1)
           try:
               if ls[j]<min:
                   min=ls[j]
           except TypeError:
               return min
           except IndexError:
               return min
           i+=1
    return min

h=5
t1=bst(h,is_perfect=True)
print(t1)
print(serch_max(t1))
print(serch_min(t1))
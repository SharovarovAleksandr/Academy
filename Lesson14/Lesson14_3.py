from binarytree import *

def del_unred_node(self,n):
    ind=0
    ls = list(self.values)

    if len(ls) == 0:
        print("Такого дерева не існує")
        return None
    elif len(ls) == 1:
        return None
    elif self.height==1:
        return None
    elif not self.is_bst:
        print("Функція del_undr_node може шукати найбільший елемент тільки у BTS. Це дерево не відповідає критеріям BTS ")
        return None
    else:
        i = 0
        j=0
        try:
            while i < self.height or ls[j] != n:
                jl =2*j+1
                jr =2*j+2
                if ls[j] > n:
                    j = jl
                elif ls[j] < n:
                    j = jr
                i += 1
        except IndexError:
            print("BTS не містить елементу ",n)
            return self
        else:
            ls[j] = None
            for i in range(j,len(ls)):
                try:
                    if ls[i]==None:
                        ls[2*i+1]=None
                        ls[2*i+2]=None
                except IndexError:
                    continue
            self=build(ls)
    return self



h=4
t1=bst(h,is_perfect=False)
print(t1)
n=int(input("Введіть ноду гілку під якою буде видалено : "))
print(del_unred_node(t1,n))
from binarytree import *
import random, math

def add_lst(tree, ls):
    if not tree.is_bst:
        print("This tree is not BST. I can not add list.")
        return None
    else:
        l = list(tree.values)
        h = tree.height
        print(l)
    if not tree.is_perfect:
        col=2 ** (h+1)-len(l)-1
        for i in range(col):
            l.append(None)
    for i in ls:
        l.append(i)
    n = len(l)
    h_new = int(math.log(n + 1, 2) - 1)
    if 2 ** (h_new + 1) - 1 < n:
        h_new += 1
    col = 2 ** (h_new + 1) - len(l) - 1
    for i in range(col):
        l.append(None)
    print(l)
    col1=(2**h_new)-1
    for i in range(col1):

        if l[i]==None and l[2*i+1]==None and  l[2*i+1]==None:
            continue
        else:

            try:
                if l[i]<l[2*i+1]:
                    print("Значение в списке не соответствует правилам BST. Замените число в списке на значение < ", l[i],
                          end=" ")
                    l[2*i+1]=(int(input()))

                if l[i]>l[2*i+2]:
                    print("Значение в списке не соответствует правилам BST. Замените число в списке на значение > ", l[i],
                          end=" ")
                    l[2*i+2]=(int(input()))

            except TypeError:
                continue
    return l

#
# h=3
# t1=bst(h,is_perfect=True)
# print(t1)
# num=6
# ls=[]
# for i in range(num):
#     ls.append(random.randint(1,100))
# print(ls)
# ls=add_lst(t1,ls)
# print(ls)
#
# t2=build(ls)
# print(t2)
# print(t2.values)

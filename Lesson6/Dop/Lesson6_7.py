def rec(list):
    if list == []:
        return 0
    else:
        n=len(list)
        s=list.pop(n-1)
        return s + rec(list)


l = [20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4, -3, 93,26 ]
l1=[]
print("SUM=", rec(l))
print("SUM=", rec(l1))

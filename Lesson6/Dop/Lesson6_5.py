def max_num(l):
    n=len(l)
    max=l[0]
    for i in range(n):
        if l[i]>max:
            max=l[i]
    return max

l=[ 20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4,-3,93]
print("max=",max_num(l))

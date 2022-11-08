st=["Home"," my", "sweet", "home", "I" ,"like", "Python!","Alarm","Made","in","China","In","god","we","trust"]
gl=["a","e","o","i","y","u","A","E","O","I","Y","U"]
print(st)
#Variant 1
st1=[i for i in st if len(i)<=5]
st2=[]
for i in st1 :
    for j in gl :
        if i[0]==j:
            st2.append(i)
            continue
print(st1)
print(st2)

#Variant 2
st1=[i for i in st if len(i)<=5 and i[0] in gl]
print (st1)



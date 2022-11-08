#Variant 1
for i in range(1900,2022):
    if i % 4==0 :
        print (i,"Високосный год")

#Variant 2
st=[i for i in range(1900,2022)  if i % 4==0 ]
print (st)

#Variant 3
for i in range(1900,2022,4):
        print (i,"Високосный год")